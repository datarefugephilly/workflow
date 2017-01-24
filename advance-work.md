
## Advance work

This document is meant for DataRescue event organizers. There are lots of ways to prepare for an event. This document highlights only the technical aspects of preparation. There are lots of logistical and other aspects to look out for as well, but this is the minimum needed to use the workflow outlined in this repository.  

Note that after an event, participants might want to continue the work remotely, and our workflow is designed to make that possible.


Before starting, your team should go through the following steps. 

### The basics
- Read through the entire workflow documentation
- Sign up for the datarefuge slack and make sure there's a channel for your event. 
- Define your teams. They are usually: Seeders/Sorters, Researchers, Harvesters, Checkers, Baggers, and Describers. Although in some cases, some of the roles can be conflated. Each team should have team leaders, aka "guides". 
- The organizers and team leaders should schedule a call with DataRefuge to go over the process. 

### Spreadsheets
- Make sure you know the spreadsheets you will be using and where to begin. Talk to a DataRefuge coordinator to establish that.
 - The goal is keep track of which URLs have already been archived and which ones have not, and avoid any duplication of efforts. 

### Crawl vs. Harvest: storage needs 
- The main triage point of the workflow is whether a URL can be automatically crawled, for instance by the Internet Archive, or whether it will need to be manually harvested.
 - The crawling process does not require any separate storage management, as the crawlable URLs are nominated to the Internet Archive, who will take care of the actual file storage after they have crawled the pages. See the [Seeders/Sorters documentation](seednsort.md) for more information on this process. 
 - Datasets harvested through the Harvest process are stored on S3 storage managed directly by DataRefuge.

### S3 storage
- You need two S3 "buckets" (i.e., directories) for your harvested files.  
 - The Harvesters will upload the files they harvest to a first bucket ("pre-bag" bucket), and then
 - The Baggers will turn those files into bags and upload the bags to the second bucket ("bag" bucket)
- Get the **name of the two s3 buckets** for your event from DataRefuge. Each event has its own, so you'll need to add that info to the S3 info for all datasets/urls you tackle at your event to make the URL of your final bags populate the right field.
 - Uploaders will need to be given **credentials for s3**. Uploaders need not be coders, but they should have a little experience working in command line, and computers with python 2.7.
 - Metadata folks will need to have **credentials for ckan**. 
1. Team leaders for the Seeders and Sorters should check in with EDGI folks for info about how to make sure that you're seeding and sorting. More info ...

1. Make sure you have a few thumb drives to handle very large data sets (above 5 Gigs)


