

# Checkers

## What do Checkers do?
Checkers inspect a harvested dataset and make sure that it is complete. The main question the checkers need to answer is "will the bag make sense to a scientist"? 

## Getting set up as a Checker
- Skills recommended for this role: in general, Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.
- Apply to become a Checker 
   - By filling out [this form](https://docs.google.com/a/temple.edu/forms/d/e/1FAIpQLSfh9YIFnDrc-Cuc0hTd-U37J3D8xw8K7VXmzWkPs6Y5Q0wfVg/viewform) 
    - Note that an email address is required to apply.
    - Note also that you should be willing to have your real name be associated with the datasets, to follow archival best practices (see [guidelines on archival best practices for Data Refuge](http://www.ppehlab.org/blogposts/2017/2/1/data-refuge-rests-on-a-clear-chain-of-custody) for more information).
- The organizers of the event (in-person or remote) will send you an invite to the [Archivers app](http://www.archivers.space/), which helps us coordinate all the data archiving work we do.
	- Click the invite link, and choose a user name and a password.    
- Make sure you have an account on the DataRefuge slack where people share expertise and answer each other's questions.
	- Ask your event organizer to send you an invite 
- You might also need to have some other software and utilities set up on your computer, depending methods you will use, when needing to harvest supplemental materials to add to a dataset.
- If you need any assistance:
 - Talk to your DataRescue Guide if you are at an in-person event
 - Or post  questions on Slack in the #Checkers channel.

## Claiming a dataset for the checking step 
  - You will work on datasets that were harvested by Harvesters. 
  - Go to the [Archivers app](http://www.archivers.space/), click `URLS` and then `FINALIZE`: all the URLs listed are ready to be checked
    - Available URLs are the ones that have not been checked out by someone else, that is, that do not have someone's name in the User column.
- Select an available URL and click its UUID to get to the detailed view, then click `Check out this URL`. It is now ready for you to work on, and no one else can do anything to it while you have it checked out. 
- While you go through the checking process, make sure to report as much information as possible in the Archivers app, as this is the place were we collectively keep track of all the work done.

## Note: URL vs UUID
The `URL` is the link to examine and harvest, and the `UUID` is a canonical ID we use to connect the url with the data in question. The UUID will have been generated earlier earlier in the process. UUID stands for Universal Unique Identifier. 

**Note: the next few steps below need to be reviewed in light of the new app-driven workflow** 

## Downloading & opening the dataset
  - Go to the URL containing the zipped dataset (provided in cell "URL from upload of zip") 
  - Download the zip file to your laptop, and unzip it.

## Checking for completeness and meaningfulness
  - Your role is to inspect the dataset and make sure that it is complete.
  - You also need to check that the dataset is *meaningful*, that is: "will the bag make sense to a scientist"? 
    - For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible for a scientist to use it.
   
## Adding missing items
  - You should add any missing file or metadata information to the dataset
  - Please refer to the [Harvesting Tookit](https://github.com/datarefugephilly/workflow/tree/FinalizeRemote-Delphine/harvesting-toolkit) for more details
 
## Re-uploading
  - If you have made any changes to the dataset, zip the all the files and upload the new resulting zip file, using the application http://drp-upload.herokuapp.com/
     - Make sure to select the name of your event in the dropdown (and "remote" if you are working remotely)
    - Note that files beyond 5 Gigs cannot be uploaded through this method
      - Please talk to your DataRescue guide/post on Slack in Checkers channel, if you have a larger file
    - The file you uploaded has now replaced the old version, and it is available at the same url (in cell "URL from upload of zip")
  - Quality assurance: 
    - To ensure that the zip file was uploaded successfully, go to the URL and download it back to your laptop. 
    - Unzip it, open it and spot check to make sure that all the files are there and seem valid.
 
## Finishing up
- In the Archivers app, make sure to fill out as much information as possible to document your work.
- Check the Finalize checkbox (on the right-hand side) to mark that step as completed. 
- Click `Save`.
- Click `Check in URL`, to release it and allow someone else to work on the next step. 

- You're done! Move on to the next URL! 
 
 <!-- - In the Uncrawlable spreadsheet, briefly describe any change you have made in cell "Any Changes?", and answer yes or no in cell "Files in  UUID.zip are all good?" -->
  
