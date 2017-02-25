# DataRescue Workflow -- Overview

This document describes the workflow we use for DataRescue activities as developed by the [DataRefuge project](http://www.ppehlab.org/) and [EDGI](https://envirodatagov.org/), both at in-person events and when people work remotely. It explains the process that a URL/dataset goes through from the time it has been identified, either by a [Seeder](seeding.md) as "uncrawlable," or by other means, until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves several stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security.

## Before You Begin
We are so glad that you are participating in this project!

<!--**[If you are an overall Coordinator](coordinator-work.md)**:
- See the description of some of the work overall coordinators do [here](coordinator-work.md)-->

### [If You Are an Event Organizer](advance-work.md)

- Learn about what you need to do to prepare the event [here](advance-work.md).

### If You Are a Regular Participant

- Get a role assignment (e.g. Seeder or Harvester), get account credentials needed for your role, and make sure you have access to the key documents and app needed to do the work. The organizers will instruct you on these steps.
- Create an account on the DataRefuge Slack using this [slack-in](https://rauchg-slackin-qonsfhhvxs.now.sh/) (or use the Slack team recommended by your event organizers). This is where people share expertise and answer each other's questions.   
- Go over the workflow documentation below and read the detailed page(s) corresponding to your role.


**********************

## Plan Overview

### 1. [Seeding](seeding.md)

Seeders canvass the resources of a given government agency, identifying important URLs. They identify whether those URLs can be crawled by the Internet Archive's webcrawler. If the URLs are crawlable, the Seeders nominate them to the End-of-Term (EOT) project. Otherwise, they add them to the Uncrawlable spreadsheet using the project's Chrome Extension.

### 2. [Researching](researching.md)

Researchers inspect the "uncrawlable" list to confirm that Seeders' assessments were correct (that is, that the URL/dataset is indeed uncrawlable), and investigate how the dataset could be best harvested. [Researching.md](researching.md) describes this process in more detail.

*We recommend that Researchers and Harvesters (see below) work together in pairs, as much communication is needed between the two roles. In some cases, one person will fulfill both roles.*

### 3. [Harvesting](harvesting.md)

Harvesters take the "uncrawlable" data and try to figure out how to actually capture it based on the recommendations of the Researchers. This is a complex task which can require substantial technical expertise, and which requires different techniques for different tasks. Harvesters should see the included [Harvesting Toolkit](harvesting.md) for more details and tools.

### 4. Checking

**Note: This role is currently performed by the Baggers, and does not exist separately.**

Checkers inspect a harvested dataset and make sure that it is complete. The main question the checkers need to answer is "will the bag make sense to a scientist"? Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.

### 5. [Bagging](bagging.md)

Baggers perform some quality assurance on the dataset to make sure the content is correct and corresponds to the original URL. Then they package the data into a bagit file (or "bag"), which includes basic technical metadata, and upload it to the final DataRefuge destination.

### 6. [Describing](describing.md)

Describers create a descriptive record in the DataRefuge CKAN repository for each bag. Then they link the record to the bag and make the record public.

**********************

## Partners

DataRescue is a broad, grassroots effort with support from numerous local and nationwide networks. [DataRefuge](http://www.ppehlab.org/datarefuge/) and [EDGI](https://envirodatagov.org/) partner with local organizers in supporting these events. See more of our institutional partners on the [DataRefuge home page](http://www.ppehlab.org/datarefuge#partners).

