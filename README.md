### MRF Conversion Tool
#### Vincent Dolciato
###### This file creation tool takes in json files from healthcare providers and converts them into a useable csv format.
###### Later this csv will be used to create a SQL table that can provide healthcare prices to clients.

-------
###### Version 1.0 Changelog:
* Created JSON to CSV functionality
* Currently the column scheme is as follows
  * billing code
  * name of procedure / medicine 
  * description of procedure / medicine
  * provider reference 
    (I understand this to be a unique identifier for a healthcare provider under the network of )
    (the insurance company.                                                                     )
    (This means that multiple providers may be listed for each billing code and therefore all   )
    (provider references are followed by a number.                                              )
 * negotiated rate 
    (I understand this to be the agreed upon price for a procedure/medicine as per the          )
    (healthcare provider. As some providers give multiple rates for the same procedure/medicine )
    (the numbering scheme is as follows                                                         )
    (negotiated_rate_PROVIDER REFERENCE_RATE NUMBER                                             )
    (ex. Provider X has rates 0, 1, 2 for some code.                                            )
    (   those rates can be found in columns 'negotiated_rate_X_0/1/2' respectively              )
 * billing class
    (Same naming scheme as negotiated rate)

###### Version 1.0 Unfinished (Plans for Version 1.1):
* Not operating on a full dataset of 500 healthcare codes 
    This was done for debugging simplicity, 500 codes will be added in next version
* No actual rates are being added to the file
* No classes are being added to the file
* It may be more readable if the columns are named after the provider reference 
    and not simply based on a count of providers for each code.
    eg. provider_reference_2760 instead of provider_reference_0/1/2/3/etc.
        negotiated_rate_2760_0/1/2/etc.
        
-------

###### Version 1.1 Changelog:
* Operating on full dataset of 500 healtchare codes
* Rates added
* Billing Classes added

###### Version 1.1 Unfinished:
* Output file has hardcoded value.
    This will remain as such for testing, prod version will output a csv filename identical to json input name
* Tests need to be ran on input files from different providers. Currently only testing MedMeutual

-------
