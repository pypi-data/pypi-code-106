#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: the user could directly input the dataframe format file generated by MetageneAnalysis.py and plot the ribosome footprint density without re-do from the bam files
			1) the input file must be python DataFrame format, and has three required columns:
				1. columns one : sample name [required].
				2. columns two : footprint density from the start codon [required].
				3. columns three: footprint density from the stop codon [required].
				4. start_lower_CI: lower confidence value of density from start codon.
				5. start_higher_CI: higher confidence value of density from start codon.
				6. stop_lower_CI: lower confidence value of density from stop codon.
				7. stop_highrt_CI: higher confidence value of density from stop codon.
			2) the output file could be pdf/png/jpg format
'''

import numpy as np
import pandas as pd
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from optparse import OptionParser
from functools import reduce
from itertools import chain
from collections import defaultdict
from .__init__ import __version__

def create_parser_for_metagene_plot():
	'''argument parser'''
	usage="usage: python %prog [options]" +"\n" + __doc__+"\n"
	parser=OptionParser(usage=usage,version=__version__)
	parser.add_option("-i","--input",action="store",type="string",dest="density_file",help="Input file in txt format.And the files has three columns; column 1: sample;columns 2: start_density; column 3: stop_density")
	parser.add_option("-d","--downstream_codon",action="store",type="int",default=500, dest="downstream_codon", help="Downstream codon corresponding to start codon (codon unit). While corresponding to stop codon, it is the upstream codon.")
	parser.add_option("-u","--upstream_codon",action="store",type="int",default=0,dest="upstream_codon",help="Upstream codon corresponding to start codon (codon unit). While corresponding to stop codon, it is the downstream codon.")
	parser.add_option("-o","--output",action="store",type="string",dest="output_prefix",help="Prefix of output files.[required]")
	parser.add_option('-g','--group',action="store",type="string",dest="group_name",help="Group name of each group separated by comma. e.g. 'si-control,si-eIF3e'")
	parser.add_option('-r','--replicate',action="store",type="string",dest="replicate_name",help="Replicate name of each group separated by comma. e.g. 'si_3e_1_80S,si_3e_2_80S__si_cttl_1_80S,si_ctrl_2_80S'")
	parser.add_option("-f","--format",action="store",type="string",dest="output_format",default='pdf',help="Output file format,'pdf','png' or 'jpg'. default=%default")
	parser.add_option("--ymax",action="store",type="float",dest="ymax",default=None,help="The max of ylim. default=%default")
	parser.add_option("--ymin",action="store",type="float",dest="ymin",default=None,help="The min of ylim. default=%default")
	parser.add_option("-U","--unit_type",action="store",type="string",dest="unit", default="codon",help="Unit type we used for metagene analysis. Either 'nt' or 'codon'. default=%default")
	parser.add_option("--slide-window",action="store",type="string",dest="slideWindow",default=None,help="Using slide window to average the density.Input a  true strings such as yes, y or 1. %default=default")
	parser.add_option("--axvline",action="store",type="float",dest="axvline",default=None,help="Position to plot vetical line")
	parser.add_option("--axhline",action="store",type="float",dest="axhline",default=None,help="Position to plot horizontal line")
	parser.add_option("--start",action="store",type="int",dest="start_position",default=5,help="The start position need to be averaged.default=%default")
	parser.add_option("--window",action="store",type="int",dest="window",default=7,help="The length of silde window. ddefault=%default")
	parser.add_option("--step",action="store",type='int',dest="step",default=1,help="The step length of slide window. default=%default")
	parser.add_option("--CI",action="store",type='float',dest="CI",default=None,help="plot the confidence intervals or not. If yes, plot the CI region(95% CI default the same as metageneAnalysis.py). else, no. default=%default")
	parser.add_option("--mode",action="store",type="string",dest="mode",default='all',help="plot all samples or just mean samples [all or mean].If choose 'all',output all samples as well as mean samples, else just mean samples.default=%default")

	return parser

def plot_density_codon_level(data,samples,Type,in_regionLengthParma,in_extendRegionLengthParma,inOutPrefix,inOutFomat,ymin,ymax,unit,axhline,axvline,confidence,text_font={"size":20,"family":"Arial","weight":"bold"},legend_font={"size":20,"family":"Arial","weight":"bold"}):
	'''plot the density dsitribution'''
	plt.rc('font',weight='bold')
	fig=plt.figure(figsize=(16,8))
	ax=fig.add_subplot(111)
	winLen=in_regionLengthParma+in_extendRegionLengthParma+1
	# font={"size":20,"family":"Arial","weight":"bold"}
	# colors="bgrcmykwbgrcmykw"
	if len(samples) <=8:
		colors=["b","orangered","green","c","m","y","k","w"]
	else:
		colors=sns.color_palette('husl',len(samples))
	for i in np.arange(len(samples)):
		if Type=="start codon":
			plt.plot(np.arange(0,winLen),data.iloc[np.where(data.iloc[:,0]==samples[i])].iloc[:,1],color=colors[i],label=samples[i],linewidth=1)
			if confidence:
				ax.fill_between(np.arange(0,winLen),data.iloc[np.where(data.iloc[:,0]==samples[i])].iloc[:,3],data.iloc[np.where(data.iloc[:,0]==samples[i])].iloc[:,4],color=colors[i],alpha=0.2)
			else:
				pass
			ax.set_xticks(np.arange(0,winLen,50))
			ax.set_xticklabels((np.arange(0,winLen,50)-in_extendRegionLengthParma))
			if axvline:
				ax.axvline(axvline,color="r",dashes=(3,2),alpha=0.5)
			else:
				pass

		else:
			plt.plot(np.arange(0,winLen),data.iloc[np.where(data.iloc[:,0]==samples[i])].iloc[:,2],color=colors[i],label=samples[i],linewidth=1)
			if confidence:
				ax.fill_between(np.arange(0,winLen),data.iloc[np.where(data.iloc[:,0]==samples[i])].iloc[:,5],data.iloc[np.where(data.iloc[:,0]==samples[i])].iloc[:,6],color=colors[i],alpha=0.2)
			else:
				pass
			ax.set_xticks(np.arange(0,winLen,50))
			ax.set_xticklabels((np.arange(0,winLen,50)-in_regionLengthParma))
			if axvline:
				ax.axvline(winLen-axvline,color="r",dashes=(3,2),alpha=0.5)
			else:
				pass

	if unit == 'codon':
		ax.set_xlabel("Distance from "+Type+' (codon)',fontdict=text_font)
	elif unit == 'nt':
		ax.set_xlabel("Distance from "+Type+' (nt)',fontdict=text_font)
	else:
		raise KeyError("KeyError:"+str(unit))
	ax.set_ylabel("Relative footprint density (AU)",fontdict=text_font)
	ax.set_title("Ribosome footprint density profiles",fontdict=text_font)
	ax.spines["top"].set_visible(False)
	ax.spines["right"].set_visible(False)
	ax.spines["bottom"].set_linewidth(2)
	ax.spines["left"].set_linewidth(2)
	ax.tick_params(which="both",width=2,labelsize=20)
	if not ymin and not ymax:
		pass
	elif not ymin and ymax:
		ax.set_ylim(0,ymax)
	elif ymin and not ymax:
		raise IOError("Please offer the ymax parameter as well!")
	elif ymin and ymax:
		ax.set_ylim(ymin,ymax)
	else:
		raise IOError("Please enter correct ymin and ymax parameters!")
	if axhline:
		ax.axhline(axhline,color="r",dashes=(2,3),clip_on=False,alpha=0.5)
	else:
		pass
	plt.legend(loc="best",prop=legend_font)
	plt.tight_layout()
	plt.savefig(inOutPrefix+"_"+Type+"."+inOutFomat,format=inOutFomat)
	plt.close()

def slide_window_average(data,samples,in_regionLengthParma,in_extendRegionLengthParma,inOutPrefix,start,window,step):
	''' Used for calculating mean density with a slide window'''
	data_average=defaultdict(dict)
	winLen=in_regionLengthParma+in_extendRegionLengthParma+1
	columns=data.columns
	flag=0
	for column in columns:
		data_average[column]=[]
		for i in np.arange(len(samples)):
			if flag == 0:
				data_average[column].extend([samples[i]]*winLen)
			else:
				tmp_data=np.zeros(winLen)
				tmp_data[0:int(start)]+=data.iloc[np.where(data.iloc[:,0]==samples[i])].loc[:,column][0:int(start)]
				tmp_data[-int(start):]+=data.iloc[np.where(data.iloc[:,0]==samples[i])].loc[:,column][-int(start):]
				for j in np.arange(start,winLen-start,step):
					tmp_data[j]+=np.mean(data.iloc[np.where(data.iloc[:,0]==samples[i])].loc[:,column][(j-int((window-1)/2)):(j+int((window-1)/2))])
				data_average[column].extend(tmp_data)
		flag+=1
	data_average=pd.DataFrame(data_average)
	data_average.to_csv(inOutPrefix+"_average_denisty.txt",sep="\t",index=0)
	return data_average

def calculate_mean_data(data,labels_dict,group_names,output_prefix):
	'''calculate mean value'''
	data_dict=defaultdict(list)
	data_mean_dict=defaultdict(dict)
	columns=data.columns.values
	for g in group_names:
		for r in labels_dict[g]:
			data_dict[g].append(data.iloc[np.where(data.iloc[:,0]==r)])

	for g in group_names:
		flag=0
		data_mean_dict[g]={}
		if len(labels_dict[g]) <1:
			raise IOError("Please reset your -g -r parameters because nothing present here.")
		elif len(labels_dict[g]) ==1:
			for column in columns:
				if flag == 0:
					data_mean_dict[g][column]=np.array([g]*data_dict[g][0].shape[0])
					flag+=1
				else:
					data_mean_dict[g][column]=list(reduce(zip,[data_dict[g][i].loc[:,column].values for i in np.arange(len(data_dict[g]))]))

		elif len(labels_dict[g])==2:
			for column in columns:
				if flag == 0:
					data_mean_dict[g][column]=np.array([g]*data_dict[g][0].shape[0])
					flag+=1
				else:
					data_mean_dict[g][column]=np.array([sum(list(chain(i))) for i in list(reduce(zip,[data_dict[g][i].loc[:,column].values for i in np.arange(len(data_dict[g]))]))])/len(labels_dict[g])

		else:
			for column in columns:
				if flag==0:
					data_mean_dict[g][column]=np.array([g]*data_dict[g][0].shape[0])
					flag+=1
				else:
					data_mean_dict[g][column]=np.array([sum(list(flatten(i))) for i in list(reduce(zip,[data_dict[g][i].loc[:,column].values for i in np.arange(len(data_dict[g]))]))])/len(labels_dict[g])


	for k,v in data_mean_dict.items():
		data_mean_dict[k]=pd.DataFrame(v)

	data_mean=pd.concat([v for v in data_mean_dict.values()])
	## write the mean density file
	data_mean.to_csv(output_prefix+"_mean_dataframe.txt",sep="\t",index=0)
	return data_mean

def flatten(xs):
	for x in xs:
		if isinstance(x,tuple):
			for xx in flatten(x):
				yield xx
		else:
			yield x

def parse_plot_density_for_CDS_metagene():
	parsed=create_parser_for_metagene_plot()
	(options,args)=parsed.parse_args()
	(data,in_regionLengthParma,in_extendRegionLengthParma,output_prefix,group_names,replicate_names,output_format,ymin,ymax,unit,axhline,axvline,start,window,step,slideWindow,CI,mode)=(options.density_file,
	options.downstream_codon,options.upstream_codon,options.output_prefix,options.group_name.strip().split(','),options.replicate_name.strip().split('__'),
	options.output_format,options.ymin,options.ymax,options.unit,options.axhline,options.axvline,options.start_position,options.window,options.step,options.slideWindow,options.CI,options.mode)
	if window%2 == 0:
		raise IOError("Please reset your --window parameter. It must be a odd number.")
	if (start-1) < (window-1)/2:
		raise IOError("Please reset your --step and --window parameters. The (window-1)/2 must be less than start-1")
	print("your input file is: "+str(data),file=sys.stderr)
	data=pd.read_csv(data,sep="\t")
	samples=np.unique(data.iloc[:,0])
	text_font={"size":30,"family":"Arial","weight":"bold"}
	legend_font={"size":30,"family":"Arial","weight":"bold"}
	text_font_mean={"size":30,"family":"Arial","weight":"bold"}
	legend_font_mean={"size":30,"family":"Arial","weight":"bold"}
	labels_dict={}
	for g,rep in zip(group_names,replicate_names):
		labels_dict[g]=rep.strip().split(',')
	##
	if len(samples) < 1:
		raise IOError("There is no samples in the file, please check your input!")
	if len(samples) == 1:

		plot_density_codon_level(data,samples,"start codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix,output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font,legend_font=legend_font)
		plot_density_codon_level(data,samples,"stop codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix,output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font,legend_font=legend_font)
		print("finished plot the ribosome footprint density",file=sys.stderr)

	## calculate the mean density
	if len(samples) >1 :
		data_mean=calculate_mean_data(data,labels_dict,group_names,output_prefix)
		samples_new=np.unique(data_mean.iloc[:,0])
		if slideWindow:
		## slide average
			data_average=slide_window_average(data,samples,in_regionLengthParma,in_extendRegionLengthParma,output_prefix,start,window,step)
			data_mean_average=slide_window_average(data_mean,samples_new,in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_mean",start,window,step)
			if mode in ['all','All','a','A']:
				plot_density_codon_level(data_average,samples,"start codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_average",output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font,legend_font=legend_font)
				plot_density_codon_level(data_average,samples,"stop codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_average",output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font,legend_font=legend_font)
			elif mode in ['mean','Mean','m','M']:
				plot_density_codon_level(data_mean_average,samples_new,"start codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_mean_average",output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font_mean,legend_font=legend_font_mean)
				plot_density_codon_level(data_mean_average,samples_new,"stop codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_mean_average",output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font_mean,legend_font=legend_font_mean)
			else:
				raise IOError("Please enter a correct --mode parameter [all or mean]")
		else:

			## plot density
			if mode in ['all','All','a','A']:
				plot_density_codon_level(data,samples,"start codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix,output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font,legend_font=legend_font)
				plot_density_codon_level(data,samples,"stop codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix,output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font,legend_font=legend_font)
			elif mode in ['mean','Mean','m','M']:
				plot_density_codon_level(data_mean,samples_new,"start codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_mean",output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font_mean,legend_font=legend_font_mean)
				plot_density_codon_level(data_mean,samples_new,"stop codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_mean",output_format,ymin,ymax,unit,axhline,axvline,CI,text_font=text_font_mean,legend_font=legend_font_mean)
			else:
				raise IOError("Please enter a correct --mode parameter [all or mean]")
			# plot_density_comparison(data_mean,samples_new,"stop codon",in_regionLengthParma,in_extendRegionLengthParma,output_prefix+"_mean",output_format,ymax,unit,text_font=text_font_mean,legend_font=legend_font_mean)
		print("finished plot the ribosome footprint density",file=sys.stderr)


def main():
	parse_plot_density_for_CDS_metagene()

if __name__ =="__main__":
	main()
