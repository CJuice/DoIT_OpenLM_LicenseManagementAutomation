"""
Process data on ArcGIS license usage in report from OpenLM and write to Excel file sheets per and for Power BI Team.

"""


def main():

    import pandas as pd
    import numpy as np

    # TODO: need to make the function read a csv of values that Pat can edit, instead of hard coded values inside script
    def workstation_to_agency(workstation_value):
        """Pat's original design for calculating Agency field value"""
        if "sha" in workstation_value:
            return 'SHA'
        elif "ad-geo" in workstation_value:
            return 'DHMH'
        elif "anlt" in workstation_value:
            return 'DOIT'
        elif "bha" in workstation_value:
            return 'DHMH'
        elif "boa" in workstation_value:
            return 'DNR'
        elif "cac" in workstation_value:
            return 'DNR'
        elif "carrhd" in workstation_value:
            return 'DHMH'
        elif "cgla" in workstation_value:
            return 'DNR'
        elif "chart" in workstation_value:
            return 'CHART'
        elif "doit" in workstation_value:
            return 'DOIT'
        elif "dt-nbar" in workstation_value:
            return 'MEMA'
        elif "dtseoc" in workstation_value:
            return 'MEMA'
        elif "f1" in workstation_value:
            return 'MDTA'
        elif "fis" in workstation_value:
            return 'DNR'
        elif "for" in workstation_value:
            return 'DNR'
        elif "hchd" in workstation_value:
            return 'DHMH'
        elif "ideha" in workstation_value:
            return 'DHMH'
        elif "ipr" in workstation_value:
            return 'DNR'
        elif "it" in workstation_value:
            return 'DOIT'
        elif "It-" in workstation_value:
            return 'DOIT'
        elif "its" in workstation_value:
            return 'DNR'
        elif "lap" in workstation_value:
            return 'DNR'
        elif "mcac" in workstation_value:
            return 'MCAC'
        elif "mda" in workstation_value:
            return 'MDA'
        elif "mdp" in workstation_value:
            return 'MDP'
        elif "met" in workstation_value:
            return 'MET'
        elif "mgs" in workstation_value:
            return 'DNR'
        elif "mht" in workstation_value:
            return 'MDP'
        elif "mmccon" in workstation_value:
            return 'MLIS'
        elif "mta" in workstation_value:
            return 'MTA'
        elif "ofkaw" in workstation_value:
            return 'DBED'
        elif "ox" in workstation_value:
            return 'DNR'
        elif "pc-" in workstation_value:
            return 'MDE'
        elif "phpa" in workstation_value:
            return 'DHMH'
        elif "prk" in workstation_value:
            return 'DNR'
        elif "ras" in workstation_value:
            return 'DNR'
        elif "scdd" in workstation_value:
            return 'MDA'
        elif "schd" in workstation_value:
            return 'DHMH'
        elif "t22" in workstation_value:
            return 'MTA'
        elif "t23" in workstation_value:
            return 'MTA'
        elif "t21" in workstation_value:
            return 'MTA'
        elif "whs" in workstation_value:
            return 'DNR'
        elif "brel" in workstation_value:
            return 'COMP'
        elif "w-7" in workstation_value:
            return 'DHCD'
        elif "cechd" in workstation_value:
            return 'DHMH'
        elif "dda-83905" in workstation_value:
            return 'DHMH'
        elif "fha-" in workstation_value:
            return 'DHMH'
        elif "hsia-" in workstation_value:
            return 'DHMH'
        elif "mhcc-" in workstation_value:
            return 'DHMH'
        elif "sandy-b" in workstation_value:
            return 'DHMH'
        elif "wic-000" in workstation_value:
            return 'DHMH'
        elif "wochd-" in workstation_value:
            return 'DHMH'
        elif "geoserv" in workstation_value:
            return 'DHMH'
        elif "vsa-" in workstation_value:
            return 'DHMH'
        elif "000_02_146299" in workstation_value:
            return 'DHR'
        elif "fa62512" in workstation_value:
            return 'DJS'
        elif "dwd27088" in workstation_value:
            return 'DLLR'
        elif "lmai" in workstation_value:
            return 'DLLR'
        elif "oos009" in workstation_value:
            return 'DNR'
        elif "minint-" in workstation_value:
            return 'MDA'
        elif "mdewin" in workstation_value:
            return 'MDE'
        elif "tr-1024352" in workstation_value:
            return 'MDE'
        elif "tr-1024362" in workstation_value:
            return 'MDE'
        elif "tr-1024368" in workstation_value:
            return 'MDE'
        elif "tr-1024371" in workstation_value:
            return 'MDE'
        elif "tr-1024385" in workstation_value:
            return 'MDE'
        elif "tr-1024386" in workstation_value:
            return 'MDE'
        elif "tr-1024388" in workstation_value:
            return 'MDE'
        elif "tr-1024393" in workstation_value:
            return 'MDE'
        elif "q13" in workstation_value:
            return 'MDOT'
        elif "va52450" in workstation_value:
            return 'MDP'
        elif "mdtagis" in workstation_value:
            return 'MDTA'
        elif "lt-thutchison" in workstation_value:
            return 'MEMA'
        elif "meshp" in workstation_value:
            return 'MPA'
        elif "mpa-hp" in workstation_value:
            return 'MPA'
        elif "s530" in workstation_value:
            return 'MPA'
        elif "s535" in workstation_value:
            return 'MPA'
        elif "s536" in workstation_value:
            return 'MPA'
        elif "s538" in workstation_value:
            return 'MPA'
        elif "s541" in workstation_value:
            return 'MPA'
        elif "s542" in workstation_value:
            return 'MPA'
        elif "msp000" in workstation_value:
            return 'MSP'
        elif "s530" in workstation_value:
            return 'MPA'
        elif "sandy-b" in workstation_value:
            return 'DHMH'
        elif "sgatesdlsl1" in workstation_value:
            return 'MLIS'
        elif "skennedydlsl1" in workstation_value:
            return 'MLIS'
        elif "smccullochdlsl1" in workstation_value:
            return 'MLIS'
        elif "srossdlsl1" in workstation_value:
            return 'MLIS'
        elif "ssd-800g1-01" in workstation_value:
            return 'MDP'
        elif "tclarkdlsl1" in workstation_value:
            return 'MLIS'
        elif "tl222845" in workstation_value:
            return 'MTA'
        elif "tl231013" in workstation_value:
            return 'MTA'
        elif "tr-1024" in workstation_value:
            return 'Training'
        elif "training" in workstation_value:
            return 'Training'
        elif "tzimmermandlsl1" in workstation_value:
            return 'MLIS'
        elif "va47" in workstation_value:
            return 'MVA'
        elif "va511" in workstation_value:
            return 'MVA'
        elif "va54" in workstation_value:
            return 'MVA'
        elif "va625" in workstation_value:
            return 'MVA'
        elif "va52450" in workstation_value:
            return 'MDOT'
        elif "vsa-" in workstation_value:
            return 'DHMH'
        elif "wic-00076933" in workstation_value:
            return 'DHMH'
        elif "wochd-7397" in workstation_value:
            return 'DHMH'
        elif "yweissmannmgal1" in workstation_value:
            return 'MLIS'
        elif "wsu00" in workstation_value:
            return 'DNR'
        else:
            return 'Research'

    data_file = r"Example Activity Report Generated by OpenLM.csv"
    output_file = r"TEST.xlsx"
    fields_to_drop = ["Version", "License Type", "Borrowed", "Server", "Vendor", "Additional Key", "Host Ids", "IP",
                      "Project", "Group", "Usage Time w/in filter period", "Consumed Tokens", "Idle Time (hours)",
                      "Token Usage Time", "Token Usage Time w/in filter period", "Session ID",
                      "Source"]
    # fields_of_interest = ["Feature", "Product", "Start Time", "End Time", "Workstation", "User Name", "First Name",
    #                       "Last Name", "Email", "Total usage time (hours)", "Usage Time w/in filter period",
    #                       "Token Usage Time w/in filter period"]
    new_fields = ["Agency", "Date", "Product_Workstation", "Product_Username"]
    excel_date_format = "YYYY-MM-DD"
    excel_datetime_format = "YYYY-MM-DD HH:MM:SS"

    # Create master dataframe from report csv file
    master_df = pd.read_csv(data_file)
    # print(master_df.info())

    # Slim size of dataframe by dropping unneeded fields
    master_df.drop(columns=fields_to_drop, inplace=True)
    # print(master_df.info())

    # Add the new fields to the master dataframe
    generic_series = pd.Series(data=np.NaN, index=master_df.index)
    for field in new_fields:
        master_df[field] = generic_series

    # NOTE: When i try to use f strings or .format to form the concatenated values I encounter weird results.
    # Calculate Product_Workstation field
    master_df["Product_Workstation"] = master_df["Product"] + "_" + master_df["Workstation"]

    # Calculate Product_Username field
    master_df["Product_Username"] = master_df["Product"] + "_" + master_df["User Name"]

    # Calculate Date field
    master_df["Start Time"] = pd.to_datetime(arg=master_df["Start Time"], dayfirst=True)
    master_df["End Time"] = pd.to_datetime(arg=master_df["End Time"], dayfirst=True)

    # Calculate Agency field
    master_df["Agency"] = workstation_to_agency(master_df["Workstation"])

    # Product_Workstation
    print(master_df.info())
    product_workstation_df = master_df[["Agency", "Product_Workstation"]]
    agency_product_gbdf = master_df.groupby(by=["Agency", "Product"])
    print(agency_product_gbdf.groups)

    # Write output datasets to excel file sheets
    # with pd.ExcelWriter(path=output_file, date_format=excel_date_format, datetime_format=excel_datetime_format) as writer:
    #     pass


if __name__ == "__main__":
    main()
