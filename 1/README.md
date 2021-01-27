#Prompt
Create a script to clone an Azure DevOps build definition to a new one named BuildMyApp.

#Solution
I had a test Server 2019 VM on my laptop, with Azure DevOps server installed, so I worked on there.

I began with the [REST API docs](https://docs.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-6.1&viewFallbackFrom=azure-devops).  It was a little bit of a wrestling contest to get DevOps server to clone an entry given just a build ID and revision, but I switched to an approach of stripping unnecessary JSON items from the response body of the origin and submitting them as part of the clone request.  The script will prompt for information as needed, and in fact, I spent a fair bit of time on readability and user-friendly features.

Nothing special is required to run; just Python with the `requests` module.
