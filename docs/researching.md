## What Do Researchers Do?

Researchers review "uncrawlables" identified during [Seeding](seeding.md), confirm the URL/dataset is indeed uncrawlable, and investigate how the dataset could be best harvested. Researchers need to have a good understanding of harvesting goals and have some familiarity with datasets.

<div class = "note">
  <strong>Recommended Skills</strong> <br />  
  Consider this path if you have strong front-end web experience and enjoy research. An understanding of how federal data is organized (e.g. where "master" datasets are) would be valuable.
</div>

## Getting Set up as a Researcher

- Event organizers (in-person or remote) will tell you how to volunteer for the Researcher role, either through Slack or a form.
    - As a result, they will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
    - Click the invite link, and choose a user name and a password.
- Create an account on the DataRefuge Slack using this [slack-in](https://rauchg-slackin-qonsfhhvxs.now.sh/) or use the Slack team recommended by your event organizers. This is where people share expertise and answer each other's questions. 
- If you need any assistance:
    - Talk to your DataRescue guide if you are at an in-person event
    - Or post questions on Slack in the `#general` channel (or other channel recommended by your event organizers).

## Researchers and Harvesters

- Researchers and Harvesters should work very closely together as their work will feed from each other and much communication is needed between the two roles.
- It may be most effective for Researchers and Harvesters to work together in pairs or small groups. In some cases, a single person might be both a Researcher and a Harvester.
- As a Researcher, make sure to check out the [Harvesters documentation](harvesting.md) to familiarize yourself with their role.

## Claiming a Dataset to Research

- Researchers work on datasets that were listed as uncrawlable by Seeders.
- Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `RESEARCH`: all the URLs listed are ready to be researched.
    - Available URLs are ones that have not been checked out by someone else, i.e. that do not have someone's name in the User column.
- Select an available URL and click its UUID to get to the detailed view, then click `Check out this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out.
- While you go through the research process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

<div class = "note">
  <strong>Note: URL vs UUID</strong> <br />  
  The <code>URL</code> is the link to examine and harvest, and the <code>UUID</code> is a canonical ID we use to connect the URL with the data in question. The UUID will have been generated earlier in the process. UUID stands for Universal Unique Identifier.
</div>

## Evaluating the Data

Go to the URL, and start inspecting the content.

### Is the data actually crawlable?

Again, see [EDGI's Guides](https://edgi-govdata-archiving.github.io/guides/) for a mostly non-technical introduction to the crawler:

- [Understanding the Internet Archive Web Crawler](https://edgi-govdata-archiving.github.io/guides/internet-archive-crawler/)
- [Seeding the Internet Archive’s Web Crawler](https://edgi-govdata-archiving.github.io/guides/seeding-internet-archive/)

Some additional technical notes for answering this:

- There is no specific file size cutoff for what is crawlable, but large files should be manually captured anyway.
- File types like ZIP, PDF, Excel, etc. are crawlable if they are linked.
- The crawler can only follow HTTP links that appear directly in the DOM at load time. (That is, they should appear as `<a href ...>` tags in the page source.)
If links are added by JavaScript or require submitting a form, they are not crawlable.
- The crawler does not tolerate web frames (but it is straightforward to inspect a page to obtain the content in the frame directly, and then nominate *that*).
- The crawler recently added the ability to crawl FTP, but we will not rely on this; we will treat resources served over FTP as uncrawlable.

**YES:**

If the URL is crawlable or you locate a crawlable URL that accesses the underlying dataset:

- Nominate it using our
  [Chrome extension](https://chrome.google.com/webstore/detail/nominationtool/abjpihafglmijnkkoppbookfkkanklok) or the [bookmarklet](http://digital2.library.unt.edu/nomination/eth2016/about/).
- Click the `Do not harvest` checkbox in the Archivers app.
<!-- why don't we ask that any more?  - Fill out cell "Seeded?" = "yes" and tell what URL you seeded. -->

**NO:**

If it is confirmed not crawlable:
<!-- Why don't we ask that any more? - Fill out the cell "Can it be crawled?" = "no" in Researcher section of the spreadsheet-->

- Search agency websites and data.gov for dataset entry points for your dataset collection.
    - Tips: Try to understand what datasets are underlying the web pages. Look for related entries in the Archivers app, and ensure that you aren't harvesting a subdirectory if you can harvest the entire directory. Often, data underlying dozens of pages or multiple "access portal" apps is also available as one structured data file.
    - Make note of any better entry point in the `Recommended Approach`field, along with any other recommendations on how to proceed with this harvest.
<!-- - Add your suggested url for harvesting the data to spreadsheet (in cell "Harvestable Data"), REALLY IMPORTANT!-->
- Add other information that could help the Harvester, such as the format (SQL, FTP, ZIP, PDF collections, etc.), approximate size, details about what you found, etc.
- Search for related URLs that might already have been listed in the Archivers app that might be covered by the same approach, so as not to duplicate work. You can search for them in the `Link URL` field.

**YES and NO:**

For example, FTP address, mixed content, big data sets:
<!--  - Fill out the cell "Can it be crawled?" = "yes & no" in Researcher section of the spreadsheet-->

- Nominate it anyway, but also follow the steps for uncrawlable content above.
- *While we understand that this may result in some dataset duplication, this is not a concern. We are ensuring that the data is fully preserved and accessible.*

## Finishing Up

- In the Archivers app, make sure to fill out as much information as possible to document your work.
- Check the Research checkbox (on the right-hand side) to mark that step as completed.
- Click `Save`.
- Click `Check in URL`, to release it and allow someone else to work on the next step.
- You're done! Move on to the next URL!

<!-- HOW DOES THIS PROCESS WORK NOW:    - If ever a day or more passed  since you originally claimed the item, update the date to today's date.
    - Note that if more than 2 days have passed since you claimed the dataset and it is still not closed, the **Date field will turn red**, signaling that someone else can claim it in your place and start working on it
      - This will avoid datasets being stuck in the middle of the workflow and not being finalized.-->