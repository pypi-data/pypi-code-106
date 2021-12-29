#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Author: Li Fajin
'''

import sys
import pysam
from itertools import groupby
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from optparse import OptionParser
from collections import defaultdict



def create_parser_for_reads_length():
	'''argument parser'''
	usage="usage: python %prog [options]"
	parser=OptionParser(usage=usage)
	parser.add_option("-i","--input",action="store",type="string",dest="bamFile",help="Input file in BAM format")
	parser.add_option("-l","--left-position",action="store",type="int",default=None, dest="left_position", help="Left position of the sequence you are interested in.")
	parser.add_option("-r","--right-position",action="store",type="int",default=None,dest="right_position",help="Right position of the sequence you are interested in.")
	parser.add_option("-o","--output",action="store",type="string",dest="output_prefix",help="Prefix of output files.[required]")
	parser.add_option("-c","--coordinateFile",action="store",type="string",dest="coorFile",
			help="The file should contain the coordinate of start and stop codon. Generated by OutputTranscriptInfo.py.[required]")
	parser.add_option('-S','--select_trans_list',action="store",type='string',dest='in_selectTrans',default=None,
			help="Selected transcript list used for metagene analysis.This files requires the first column must be the transcript ID  with a column name. default=%default")
	parser.add_option("--type",action='store',type='string',dest='type',default='CDS',help='Type of regions.[CDS/5UTR/3UTR].default=%default')
	parser.add_option('--id-type',action="store",type="string",dest="id_type",default="transcript_id",
			help="define the id type users input. the default is transcript id, if not, will be transformed into transcript id. default=%default")
	return parser




def reload_transcripts_information(longestTransFile):
	selectTrans=set()
	transLengthDict={}
	cdsLengthDict={}
	startCodonCoorDict={}
	stopCodonCoorDict={}
	transID2geneID={}
	transID2geneName={}
	transID2ChromDict={}
	with open(longestTransFile,'r') as f:
		for line in f:
			if line.strip()=='':
				continue
			if line.strip().split("\t")[0] == 'chrom':
				continue
			chrom=line.strip().split("\t")[0]
			transID=line.strip().split("\t")[1]
			geneID=line.strip().split("\t")[3]
			geneName=line.strip().split("\t")[4]
			startCodon=int(line.strip().split("\t")[8])
			stopCodon=int(line.strip().split("\t")[9])
			cds_length=int(line.strip().split("\t")[10])
			transLength=int(line.strip().split("\t")[13])
			selectTrans.add(transID)
			transLengthDict[transID]=transLength
			startCodonCoorDict[transID]=startCodon
			stopCodonCoorDict[transID]=stopCodon
			transID2geneID[transID]=geneID
			transID2geneName[transID]=geneName
			cdsLengthDict[transID]=cds_length
			transID2ChromDict[transID]=chrom
			# print(transID,geneID,geneName,startCodon,stopCodon,transLength)
	print(str(len(selectTrans))+'  transcripts will be used in the follow analysis.\n', file=sys.stderr)
	return selectTrans,transLengthDict,startCodonCoorDict,stopCodonCoorDict,transID2geneID,transID2geneName,cdsLengthDict,transID2ChromDict

def IDTransform(coorFile,in_selectTrans,id_type):
	selectTrans,transLengthDict,startCodonCoorDict,stopCodonCoorDict,transID2geneID,transID2geneName,cdsLengthDict,transID2ChromDict=reload_transcripts_information(coorFile)
	geneID2transID={v:k for k,v in transID2geneID.items()}
	geneName2transID={v:k for k,v in transID2geneName.items()}
	if in_selectTrans:
		select_trans=pd.read_csv(in_selectTrans,sep="\t")
		select_trans=set(select_trans.iloc[:,0].values)
		if id_type == 'transcript_id':
			select_trans=select_trans.intersection(selectTrans)
			print("There are " + str(len(select_trans)) + " transcripts from "+in_selectTrans+" used for following analysis.",file=sys.stderr)
		elif id_type == 'gene_id':
			tmp=[geneID2transID[gene_id] for gene_id in select_trans if gene_id in geneID2transID]
			select_trans=set(tmp)
			select_trans=select_trans.intersection(selectTrans)
			print("There are " + str(len(select_trans))+" gene id could be transformed into transcript id and used for following analysis.",file=sys.stderr)
		elif id_type == 'gene_name' or id_type=='gene_symbol':
			tmp=[geneName2transID[gene_name] for gene_name in select_trans if gene_name in geneName2transID]
			select_trans=set(tmp)
			select_trans=select_trans.intersection(selectTrans)
			print("There are " + str(len(select_trans))+" gene symbol could be transformed into transcript id and used for following analysis.",file=sys.stderr)
		else:
			raise IOError("Please input a approproate id_type parameters.[transcript_id/gene_id/gene_name/]")
	else:
		select_trans=selectTrans
	return select_trans,transLengthDict,startCodonCoorDict,stopCodonCoorDict,cdsLengthDict

def OutputReadsLength(in_bamFile,in_selectTrans,transLengthDict,startCodonCoorDict,stopCodonCoorDict,left_position,right_position,Type):
	readLengthList=[]
	pysamFile=pysam.AlignmentFile(in_bamFile,'rb')
	if not in_selectTrans:
		selectTrans=pysamFile.references
	elif in_selectTrans:
		selectTrans=set(pysamFile.references).intersection(in_selectTrans)
	for trans in selectTrans:
		leftCoor =int(startCodonCoorDict[trans])-1
		rightCoor=int(stopCodonCoorDict[trans])-3
		for record in pysamFile.fetch(trans):
			if record.flag==16 or record.flag==272:
				continue
			pos=record.pos
			readLength=record.query_length
			if Type.upper()=='5UTR':
				if pos < leftCoor:
					readLengthList.append(readLength)
			elif Type.upper()=='3UTR':
				if pos > rightCoor:
					readLengthList.append(readLength)
			elif Type.upper()=='CDS':
				if left_position and right_position:
					if pos>=(leftCoor+left_position-1) and pos <= (leftCoor+right_position):
						readLengthList.append(readLength)
				elif not left_position and not right_position:
					if pos >=leftCoor and pos < rightCoor:
						readLengthList.append(readLength)
				else:
					raise IOError("Please input -l and -r parameters!")
			else:
				raise IOError("--type [CDS|5UTR|3UTR]")
	return readLengthList

def plot_reads_length(readLengthList,output_prefix,text_font={"size":20,"family":"Arial","weight":"bold"}):
	'''
	plot length distribution
	'''
	values=readLengthList
	plt.rc('font',weight='bold')
	fig=plt.figure(figsize=(5,4))
	ax=fig.add_subplot(111)
	plt.hist(values,bins=40,color="b",width=0.5,alpha=0.9)
	ax.spines["top"].set_linewidth(2)
	ax.spines["right"].set_linewidth(2)
	ax.spines["bottom"].set_linewidth(2)
	ax.spines["left"].set_linewidth(2)
	ax.set_xlabel("Length of reads",fontdict=text_font)
	ax.set_ylabel("Read Counts",fontdict=text_font)
	# ax.set_xticks(np.arange(0,50,5))
	# ax.set_xticklabels((np.arange(0,50,5)))
	ax.tick_params(which="both",width=2,labelsize=10)
	plt.tight_layout()
	plt.savefig(output_prefix+"_reads_length.pdf")
	plt.close()

def parse_reads_length():
    parser=create_parser_for_reads_length()
    (options,args)=parser.parse_args()
    (bamFile,left_position,right_position,output_prefix,coorFile,in_selectTrans,Type,id_type)=(options.bamFile,options.left_position,options.right_position,options.output_prefix,options.coorFile,options.in_selectTrans,options.type,options.id_type)
    select_trans,transLengthDict,startCodonCoorDict,stopCodonCoorDict,cdsLengthDict=IDTransform(coorFile,in_selectTrans,id_type)
    print("Starting...")
    readLengthList=OutputReadsLength(bamFile,select_trans,transLengthDict,startCodonCoorDict,stopCodonCoorDict,left_position,right_position,Type)
    plot_reads_length(readLengthList,output_prefix,text_font={"size":20,"family":"Arial","weight":"bold"})
    readLengthListDB=pd.DataFrame(readLengthList)
    readLengthListDB.to_csv(output_prefix+"_"+Type+"_read_length.txt",index=0,header=0)
    print("Finish!")

def main():
	parse_reads_length()

if __name__=="__main__":
    main()