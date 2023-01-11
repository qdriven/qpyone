# #!/usr/bin/env python
#
# from atlassian import Confluence
#
#
# confluence = Confluence(url="http://localhost:8090", username="admin", password="admin")
#
# status = confluence.create_page(
#     space="DEMO",
#     title="This is the title",
#     body="This is the body. You can use <strong>HTML tags</strong>!",
# )
#
# print(status)
#
# from atlassian import Jira
#
#
# jira = Jira(url="http://localhost:8080", username="admin", password="admin")
# JQL = 'project = DEMO AND status IN ("To Do", "In Progress") ORDER BY issuekey'
# data = jira.jql(JQL)
# print(data)
#
# from atlassian import Bitbucket
#
#
# bitbucket = Bitbucket(url="http://localhost:7990", username="admin", password="admin")
#
# data = bitbucket.project_list()
# print(data)
#
# from atlassian import ServiceDesk
#
#
# sd = ServiceDesk(url="http://localhost:7990", username="admin", password="admin")
#
# data = sd.get_my_customer_requests()
# print(data)
#
# from atlassian import Insight
#
#
# insight = Insight(url="http://localhost:7990", username="admin", password="admin")
#
# data = insight.get_object(88)
# print(data)
#
# from atlassian import Xray
#
#
# xr = Xray(url="http://localhost:7990", username="admin", password="admin")
#
# data = xr.get_tests("TEST-001")
# print(data)
#
# from atlassian import Bamboo
#
#
# bamboo = Bamboo(url="http://localhost:6990/bamboo/", token="<TOKEN>")
#
# data = bamboo.get_elastic_configurations()
# print(data)
