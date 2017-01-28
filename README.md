# DataRescue Workflow -- Overview

This document describes the workflow we use for the [DataRefuge project](http://www.ppehlab.org/), both at in-person events and when people work remotely.

## Our Approach

The [Internet Archive](https://archive.org/) already has an infrastructure in
place for archiving simple web content. At the end of a US presidential term,
the IA makes a [particular effort](http://eotarchive.cdlib.org/2016.html) to
capture US government websites (.gov and .mil). When possible, we leverage these
resources: we direct the Internet Archive to important pages to be captured.
Some web resources cannot be effectively captured by the IA, such as
interactive content or large structued data sets. These we capture manually,
label in a standard way, and upload to a ckan data catalog.

This document explains the process that a url/dataset goes through from the time it has been identified by a [seeder & sorter](https://github.com/datarefugephilly/workflow/blob/master/seednsort.md) as "uncrawlable" until it is made available as a record in the [datarefuge.org](http://www.datarefuge.org) ckan data catalog. The process involves several distinct stages, and is designed to maximize smooth hand-offs so that each phase is handled by someone with distinct expertise in the area they're tackling, while the data is always being tracked for security.

## Before you begin
We are so glad that you are participating in this project!
- If you are an event organizer: learn about [what you need to do to prepare the event](advance-work.md).
- If you are a regular participant: get a role assignment (e.g., Seeder, or Harvester), get account credentials needed for your role, and go over the workflow corresponding to your role. 

## Plan Overview
### 1. [Seeders/Sorters](seednsort.md)
Seeders and Sorters canvass the resources of a given government agency, identifying important URLs. They identify whether those URLs can be crawled by the Internet Archive's webcrawler. If the URLs are crawlable, the Seeders/Sorters nominate them to the End-of-Term (EOT) project, otherwise they add them to the Uncrawlable spreadsheet using the project's Chrome Extension.

### 2. [Researchers](research.md)
Researchers inspect the "uncrawlable" list to confirm that seeders' assessments were correct (that is, that the URL/dataset is indeed uncrawlable). [Research.md](research.md) describes this process in more detail. 

*Often this step is incorporated into either "Seeding and Sorting" or "Harvesting".*

### 3. [Harvesters](harvesting-toolkit)
Harvesters take the "uncrawlable" data and try to figure out how to capture it. This is a complex task which can require substantial technical expertise, and which requires different techniques for different tasks. Harvesters should see the included [Harvesting Toolkit](./harvesting-toolkit) for more details and tools. 

### 4. [Checkers](checking.md)
Checkers inspect a harvested dataset and make sure that it is complete. The main question the checkers need to answer is "will the bag make sense to a scientist"? Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.

### 5. [Baggers](bagging.md)
- Do some quality assurance on the dataset to make sure the content is correct and corresponds to what was described in the spreadsheet
- Package the data into a bagit file (or "bag"), which includes basic technical metadata and upload it to final DataRefuge destination.


### 7. [Describers](metadata.md)
- Creates a CKan record for this S3 resource
- Links bag, makes public
