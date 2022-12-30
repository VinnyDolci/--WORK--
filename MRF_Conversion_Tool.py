# This is a program to convert JSON data to CSV format
# Vincent Dolciato
# Version 1.1

import json
import csv

# 500 healthcare codes required for display to clients
masterCodes = ["J0702","J1745","G0102","G0103","G0121","G0105","S0285","G0289","G0120","460","470","473","743","1960","1961","1967","1968","10005","10021","10040","10060","10140","10160","11000","11056","11102","11103","11200","11401","11422","11602","11721","11730","11900","12001","12011","17000","17003","17110","17111","17250","17311","19120","20550","20551","20553","20600","20605","20610","20612","27440","27441","27442","27443","27445","27446","28296","29826","29848","29880","29881","29888","30520","31231","31237","31575","36415","36471","36475","36478","42820","42826","42830","43235","43239","43846","44388","44389","44394","45378","45379","45380","45381","45382","45384","45385","45386","45388","45390","45391","45392","45398","47562","47563","49505","49585","49650","50590","51741","51798","52000","52310","52332","55250","55700","55866","57022","57288","57454","58100","58558","58563","58565","58571","58661","58662","58671","59000","59025","59400","59409","59410","59414","59425","59426","59510","59514","59515","59610","59612","59614","62322","62323","63030","64483","64493","64721","66821","66984","67028","69210","69436","70450","70486","70491","70551","70553","71045","71046","71047","71048","71101","71250","71260","71275","72040","72050","72070","72072","72100","72110","72131","72141","72146","72148","72156","72157","72158","72170","72192","72193","72195","72197","73000","73030","73070","73080","73090","73100","73110","73120","73130","73140","73221","73560","73562","73564","73565","73590","73600","73610","73620","73630","73650","73660","73700","73718","73721","73722","73723","74022","74150","74160","74170","74176","74177","74178","74181","74183","76000","76512","76514","76536","76642","76700","76705","76770","76775","76801","76805","76811","76813","76815","76817","76818","76819","76830","76831","76856","76857","76870","76872","76882","77047","77065","77066","77067","77080","77385","77386","77387","77412","78014","78306","78452","78815","80048","80050","80051","80053","80055","80061","80069","80074","80076","80081","80197","80307","81000","81001","81002","81003","81025","82043","82044","82248","82306","82553","82570","82607","82627","82670","82728","82784","82803","82947","82950","82951","83001","83002","83013","83036","83516","83540","83550","83655","83718","83880","84134","84153","84154","84436","84439","84443","84460","84480","84484","84703","85007","85018","85025","85027","85610","85730","86039","86147","86200","86300","86304","86336","86592","86644","86665","86677","86703","86704","86708","86762","86765","86780","86803","86850","87040","87046","87070","87077","87081","87086","87088","87101","87186","87205","87210","87324","87389","87491","87510","87591","87624","87653","87661","87801","87804","87807","87880","88112","88141","88142","88150","88175","88305","88312","88313","88342","90460","90471","90474","90632","90633","90649","90656","90658","90672","90681","90686","90707","90710","90715","90716","90732","90734","90736","90746","90791","90792","90832","90833","90834","90836","90837","90838","90839","90840","90846","90847","90853","92002","92004","92012","92014","92083","92133","92507","92523","92552","93000","93015","93303","93306","93307","93320","93350","93452","93798","93880","93922","93970","93971","94010","94060","94375","94726","94727","94729","95004","95115","95117","95810","95811","95860","95861","95886","96110","96365","96366","96374","96375","96376","96415","96417","97010","97012","97014","97016","97026","97032","97033","97035","97110","97112","97113","97116","97124","97140","97530","97535","97597","97811","97813","98940","98941","98943","98966","98967","98968","98970","98971","98972","99051","99173","99202","99203","99204","99205","99211","99212","99213","99214","99215","99243","99244","99283","99284","99285","99381","99382","99383","99384","99385","99386","99387","99391","99392","99393","99394","99395","99396","99397","99421","99422","99441","99442","99443"]
#masterCodes = ["J1745", "99393", "82607", "A7037"] # Used for testing and debugging

masterCodes.sort()

print('--------------------------------------------------------------------------------------------------')
print('You are running the MRF File Converter Tool by Vincent Dolciato v.1.0')
print('')
dir = input('Please enter the full directory of the file you would like to open:')
fName = input('Please enter the full name of the JSON file you would like to open without filetype extension (CASE SENSITIVE):')

print('You have selected the file ' + fName)

# Opens the file recieved as input
# If file is not found or otherwise unable to be opened, asks the user to try again
# Note: It does not ask for a new directory. Assumed that directory is correct.
while True:
    try:
        f = open(dir + fName + ".json")
        print ('File opened successfully :)')
        break
    except IOError:
        fName = input('Could not open file! Please retype name and try again.')

# Json data object of the file
MRF = json.loads(f.read())

# Lists used in constructing data objects
FiveHundred = []
references = []
prices = []

# Data objects
reference_ = ""
prices_ = ""

# Starter list for CSV object, appended to inside loop
fields = ['billing_code', 'name', 'description', 'provider_reference_0', 'negotiated_rate_0_0', 'billing_class_0_0']

# Initialized list, will be populated with dictionaries for CSV creation
entriesDict = []

# Initialized location within the dictionary structure. Used when updating dictionaries within entriesDict
entryLocation = -1

temp = 0

# Begin loop of json object
# Goes through every item inside of "in_network"
for i in MRF["in_network"]:
    
    # Only operates on items that have a billing code identical to the master list
    for j in masterCodes:
        if i["billing_code"] == j:

            entryLocation += 1

            # Code-Name-Description string. Used in creating text file
            CND = i["billing_code"] + " | "  + i["name"] + " | " + i["description"] + " | "

            # Adding new dictionary to the end of entriesDict with billing_code, name, description entries
            entriesDict.append({'billing_code': i["billing_code"], 'name': i["name"], 'description': i["description"]})
            
            # Initialize list for keeping track of rate info, used in creating string for text file
            rateInfo = []            

            # Count of how many provider references each billing code has
            # Necessary for both column creation and dictionary entries
            providerRefCount = 0

            # Debugging
            #print('Billing Code: ' + str(i["billing_code"]))

            # Begin loop of every item within negotiated rates of the current billing code
            for k in i["negotiated_rates"]:

                # Begin loop of every provider reference for the current billing code
                for l in k["provider_references"]:

                    # Debugging
                    #print('Provider Reference Count: ' + str(providerRefCount))

                    # Used for creating columns
                    # Only makes a new provider reference column if it does not exist
                    if fields.count('provider_reference_' + str(providerRefCount)) == 0:
                        fields.append('provider_reference_' + str(providerRefCount))

                    # String for text file
                    ref = "Provider Reference:" + str(l)

                    # Updates the dictionary at our location with a provider reference entry
                    entriesDict[entryLocation].update({'provider_reference_' + str(providerRefCount): str(l)})                    

                    # String for text file
                    ratesAndClass = ""

                    # Count of how many negotiated rates are given for current billing code
                    # Each rate also has a billing class so their counts are the same
                    rateAndClassCount = 0

                    # Begin loop of prices listed for each provider reference of the billing code
                    for l in k["negotiated_prices"]:

                        # Debugging
                        #print('Rate And Class Count: ' + str(rateAndClassCount))

                        # Determine if a column exists for the count of the rate on this provider reference
                        # If first rate of this provider, get the index of the column for this provider reference + 1
                        #       then insert new columns for this rate count on this provider
                        # If multiple rates for same provider, get the index for the highest existing rate + 1
                        #       then insert new columns for this rate count on this provider
                        # Note: Billing class and negotiated rate are inserted in reverse order                      
                        if fields.count('negotiated_rate_' + str(providerRefCount) + '_' + str(rateAndClassCount)) == 0:                                
                            if rateAndClassCount == 0:

                                index = fields.index('provider_reference_' + str(providerRefCount)) + 1                                    
                                fields.insert(index, 'billing_class_' + str(providerRefCount) + '_' + str(rateAndClassCount))
                                fields.insert(index, 'negotiated_rate_' + str(providerRefCount) + '_' + str(rateAndClassCount))

                            elif rateAndClassCount > 0:  

                                index = fields.index('billing_class_' + str(providerRefCount) + '_' + str(rateAndClassCount - 1)) + 1
                                fields.insert(index, 'billing_class_' + str(providerRefCount) + '_' + str(rateAndClassCount))
                                fields.insert(index, 'negotiated_rate_' + str(providerRefCount) + '_' + str(rateAndClassCount))
                        
                        # Update the dictionary entry at current location with entry for the rate and class corresponding
                        #   to the count of provider references _ count of rates for particular provider
                        entriesDict[entryLocation].update({'negotiated_rate_' + str(providerRefCount) + '_' + str(rateAndClassCount): str(l["negotiated_rate"])})
                        entriesDict[entryLocation].update({'billing_class_' + str(providerRefCount) + '_' + str(rateAndClassCount): str(l["billing_class"])})
                        ratesAndClass += " | Negotiated Rate: " + str(l["negotiated_rate"]) + " | Billing Class: " + l["billing_class"]
                        
                        # Increment how many rates exist for this provider
                        rateAndClassCount += 1

                    # Increment how many providers exist for this code
                    providerRefCount += 1
                
                # String for text file
                rateInfo.append(ref + ratesAndClass)

            # Filling string for text file
            nr = ""
            for r in rateInfo:
                nr += r + " | "
            FiveHundred.append(CND + nr)
            references.clear()
            prices.clear()

FiveHundred.sort()

# Debugging
#print("Billing Code | Name | Description")
#for i in FiveHundred:
#    print(i)

# CSV file to be created
filename = 'autocreation.csv'

# Creating CSV file
with open(filename, 'w') as csvfile:

    writer = csv.DictWriter(csvfile, fieldnames = fields, lineterminator='\n')

    writer.writeheader()

    writer.writerows(entriesDict)

    print("CSV Created Successfully")

# Creating text file
t = open(fName + ".txt", "w")
for i in FiveHundred:
    t.write(i)
    t.write("\n")
    #print("file has been written")
t.close

f.close()
