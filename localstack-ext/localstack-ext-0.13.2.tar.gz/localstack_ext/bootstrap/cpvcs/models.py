from datetime import datetime
NQYCw=str
NQYCs=int
NQYCq=super
NQYCL=False
NQYCk=isinstance
NQYCg=hash
NQYCc=bool
NQYCH=True
NQYCb=list
NQYCB=map
NQYCl=None
from typing import Set
from localstack_ext.bootstrap.cpvcs.constants import(COMMIT_TXT_LAYOUT,REV_TXT_LAYOUT,STATE_TXT_LAYOUT,STATE_TXT_METADATA,VER_TXT_LAYOUT)
class CPVCSObj:
 def __init__(self,hash_ref:NQYCw):
  self.hash_ref:NQYCw=hash_ref
class StateFileRef(CPVCSObj):
 txt_layout=STATE_TXT_LAYOUT
 metadata_layout=STATE_TXT_METADATA
 def __init__(self,hash_ref:NQYCw,rel_path:NQYCw,file_name:NQYCw,size:NQYCs,service:NQYCw,region:NQYCw):
  NQYCq(StateFileRef,self).__init__(hash_ref)
  self.rel_path:NQYCw=rel_path
  self.file_name:NQYCw=file_name
  self.size:NQYCs=size
  self.service:NQYCw=service
  self.region:NQYCw=region
 def __str__(self):
  return self.txt_layout.format(size=self.size,service=self.service,region=self.region,hash_ref=self.hash_ref,file_name=self.file_name,rel_path=self.rel_path)
 def __eq__(self,other):
  if not other:
   return NQYCL
  if not NQYCk(other,StateFileRef):
   return NQYCL
  return(self.hash_ref==other.hash_ref and self.region==other.region and self.service==self.service and self.file_name==other.file_name and self.size==other.size)
 def __hash__(self):
  return NQYCg((self.hash_ref,self.region,self.service,self.file_name,self.size))
 def congruent(self,other)->NQYCc:
  if not other:
   return NQYCL
  if not NQYCk(other,StateFileRef):
   return NQYCL
  return(self.region==other.region and self.service==other.service and self.file_name==other.file_name and self.rel_path==other.rel_path)
 def any_congruence(self,others)->NQYCc:
  for other in others:
   if self.congruent(other):
    return NQYCH
  return NQYCL
 def metadata(self)->NQYCw:
  return self.metadata_layout.format(size=self.size,service=self.service,region=self.region)
class CPVCSNode(CPVCSObj):
 def __init__(self,hash_ref:NQYCw,state_files:Set[StateFileRef],parent_ptr:NQYCw):
  NQYCq(CPVCSNode,self).__init__(hash_ref)
  self.state_files:Set[StateFileRef]=state_files
  self.parent_ptr:NQYCw=parent_ptr
 def state_files_info(self)->NQYCw:
  return "\n".join(NQYCb(NQYCB(lambda state_file:NQYCw(state_file),self.state_files)))
class Commit:
 txt_layout=COMMIT_TXT_LAYOUT
 def __init__(self,tail_ptr:NQYCw,head_ptr:NQYCw,message:NQYCw,timestamp:NQYCw=NQYCw(datetime.now().timestamp()),delta_log_ptr:NQYCw=NQYCl):
  self.tail_ptr:NQYCw=tail_ptr
  self.head_ptr:NQYCw=head_ptr
  self.message:NQYCw=message
  self.timestamp:NQYCw=timestamp
  self.delta_log_ptr:NQYCw=delta_log_ptr
 def __str__(self):
  return self.txt_layout.format(tail_ptr=self.tail_ptr,head_ptr=self.head_ptr,message=self.message,timestamp=self.timestamp,log_hash=self.delta_log_ptr)
 def info_str(self,from_node:NQYCw,to_node:NQYCw)->NQYCw:
  return f"from: {from_node}, to: {to_node}, message: {self.message}, time: {datetime.fromtimestamp(float(self.timestamp))}"
class Revision(CPVCSNode):
 txt_layout=REV_TXT_LAYOUT
 def __init__(self,hash_ref:NQYCw,state_files:Set[StateFileRef],parent_ptr:NQYCw,creator:NQYCw,rid:NQYCw,revision_number:NQYCs,assoc_commit:Commit=NQYCl):
  NQYCq(Revision,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator:NQYCw=creator
  self.rid:NQYCw=rid
  self.revision_number:NQYCs=revision_number
  self.assoc_commit=assoc_commit
 def __str__(self):
  return self.txt_layout.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,rid=self.rid,rev_no=self.revision_number,state_files=";".join(NQYCB(lambda state_file:NQYCw(state_file),self.state_files))if self.state_files else "",assoc_commit=self.assoc_commit)
class Version(CPVCSNode):
 txt_layout=VER_TXT_LAYOUT
 def __init__(self,hash_ref:NQYCw,state_files:Set[StateFileRef],parent_ptr:NQYCw,creator:NQYCw,comment:NQYCw,active_revision_ptr:NQYCw,outgoing_revision_ptrs:Set[NQYCw],incoming_revision_ptr:NQYCw,version_number:NQYCs):
  NQYCq(Version,self).__init__(hash_ref,state_files,parent_ptr)
  self.creator=creator
  self.comment=comment
  self.active_revision_ptr=active_revision_ptr
  self.outgoing_revision_ptrs=outgoing_revision_ptrs
  self.incoming_revision_ptr=incoming_revision_ptr
  self.version_number=version_number
 def __str__(self):
  return VER_TXT_LAYOUT.format(hash_ref=self.hash_ref,parent=self.parent_ptr,creator=self.creator,comment=self.comment,version_number=self.version_number,active_revision=self.active_revision_ptr,outgoing_revisions=";".join(self.outgoing_revision_ptrs),incoming_revision=self.incoming_revision_ptr,state_files=";".join(NQYCB(lambda stat_file:NQYCw(stat_file),self.state_files))if self.state_files else "")
 def info_str(self):
  return f"{self.version_number}, {self.creator}, {self.comment}"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
