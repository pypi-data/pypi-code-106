from localstack.utils.aws import aws_models
ohdOa=super
ohdOW=None
ohdOT=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ohdOa(LambdaLayer,self).__init__(arn)
  self.cwd=ohdOW
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.ohdOT.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(RDSDatabase,self).__init__(ohdOT,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(RDSCluster,self).__init__(ohdOT,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(AppSyncAPI,self).__init__(ohdOT,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(AmplifyApp,self).__init__(ohdOT,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(ElastiCacheCluster,self).__init__(ohdOT,env=env)
class TransferServer(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(TransferServer,self).__init__(ohdOT,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(CloudFrontDistribution,self).__init__(ohdOT,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,ohdOT,env=ohdOW):
  ohdOa(CodeCommitRepository,self).__init__(ohdOT,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
