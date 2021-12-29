from localstack.utils.aws import aws_models
mjIDu=super
mjIDc=None
mjIDz=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  mjIDu(LambdaLayer,self).__init__(arn)
  self.cwd=mjIDc
  self.runtime=""
  self.handler=""
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.mjIDz.split(":")[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(RDSDatabase,self).__init__(mjIDz,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(RDSCluster,self).__init__(mjIDz,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(AppSyncAPI,self).__init__(mjIDz,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(AmplifyApp,self).__init__(mjIDz,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(ElastiCacheCluster,self).__init__(mjIDz,env=env)
class TransferServer(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(TransferServer,self).__init__(mjIDz,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(CloudFrontDistribution,self).__init__(mjIDz,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,mjIDz,env=mjIDc):
  mjIDu(CodeCommitRepository,self).__init__(mjIDz,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
