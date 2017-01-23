

# Checkers

- Getting set up as a Checker
  - Talk to your DataRescue guide to make sure you can become a Checker.
    - In general, Checkers need to have an in-depth understanding of harvesting goals and potential content variations for datasets.
  - Get set up wit the app http://drp-upload.herokuapp.com/
    - This include getting an account for the app and getting the account ok'd by the DataRescue guide.
  - Contact your DataRescue guide, if you need any assistance.

- Claiming a dataset for checking step 
  - You will work on datasets that were harvested by Harvesters. 
  - Go to the Unscrawlable spreadsheet, and look for a dataset that has the status "Harvester status indicator" = Closed
  - Claim it by entering your slack handle with the status "Open" and today's date in the cell "Checker status indicator" in Checker section, for instance: 
  ```
  @khdelphine open 1/22/2017
  ```
  
- Downloading & opening the dataset
  - Go to the URL containing the zipped dataset (in cell "URL from upload of zip", in the Harvester section) 
  - Download the zip file to your laptop, and unzip it.

- Checking for completeness and meaningfulness
  - Your role is to inspect the dataset and make sure that it is complete.
  - You also need to check that the dataset is *meaningful* 
    - This is: "will the bag make sense to a scientist"? 
    - For instance, if a dataset is composed of a spreadsheet without any accompanying key or explanation of what the data represents, it might be completely impossible to a scientist to use it.
   
- Adding missing items
  - You should add any missing file or metadata information to the dataset
  - Please refer to the [Harvesting Tookit](https://github.com/datarefugephilly/workflow/tree/FinalizeRemote-Delphine/harvesting-toolkit) for more details
 
- If you have made any changes to the dataset, zip the all the files and re-upload the resulting single zip file, using the 
