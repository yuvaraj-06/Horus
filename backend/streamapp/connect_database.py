from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
class Database:
    def __init__(self):

        cloud_config= {
            'secure_connect_bundle': 'secure-connect-oynx.zip'
        }
        auth_provider = PlainTextAuthProvider('WeNyesIImgqKTzAjdWqscLGg', 'x_LceN5ffvdJzZsiuX,+jqfrJ_kXghX7KcKNmMIBWZH0eSDXHZEZJX0.3wpG4GoSiU0n4zgf_7FMF8itLl1Meu6PcRzPDd4O8z7j9hLB3fmUxk,Wwa0+dHo3ht_.NWYD')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        self.session.set_keyspace('remote')
        self.col=["id,name,password,github_id,jira,messager_id,prod_score,emotion_score,mentalhealth_score,feedback"]
        self.session.row_factory = dict_factory
    def create_table(self,name):
        query="CREATE TABLE "+name+" ( id text,name text,password text,github_id text,jira text,messager_id text,prod_score text,emotion_score text,mentalhealth_score text,feedback text,PRIMARY KEY(id));"
        a=self.session.execute_async(query)
        a.result()
        print("creation done")
    def insert(self,name,cols,col,val):
        que="INSERT INTO "+name+" " +cols+" VALUES "+"("+"?,"*len(col)+")"
        que=que[:-2]+");"
        print(que)
        insert_statement = self.session.prepare(que)
        print(val)
        a=self.session.execute(insert_statement, val)
        
        print("inserstion done")
    def show(self,name):
        query = "SELECT * FROM "+name
        a=self.session.execute(query)
       # a=a.result()
        #print(a[i])
        l=[]
        for i in a:
            l.append(i)
        return l
        
name="employee_table"
#col=["id","name"]
#print("INSERT INTO "+name+str(tuple(col))+") VALUES "+"("+"?,"*len(col)+");")
#p=Database()
#p.create_table(name)
#["id,name,password,github_id,jira,messager_id,prod_score,emotion_score,mentalhealth_score,feedback"]
#col=["id","name","password","github_id","jira","messager_id","prod_score","emotion_score","mentalhealth_score","feedback"]
#val=["1","yuvaraj","1234","yuvaraj-06","yuvaraj06","yuvarajcoder@gmail.com","1","['sad','happy']","50","60"]
#s=' ("id","name","password","github_id","jira","messager_id","prod_score","emotion_score","mentalhealth_score","feedback") '
#p.insert(name,' ("id","password") ',["id","password"],["1","raju1234"])
#print(p.show(name))
