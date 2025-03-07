Genat Iso Parser

An iso message bulk editor and parsor.

Usage Example:
    '''
    +---------------------------+
    |       ISO STREAMING       |
    +---------------------------+
    * instantiate an instance of IsoStream
    iso = IsoStream()
    
    * change any field value of your choice
    iso.change_field(2, '9999999999999999')
    
    * remove any number of fields of your choice
    iso.remove_fields(3, 4)

    * append a field alomg with value
    iso.append_field(99, 'idugfhdisuo')

    * allow length of fields(if there is any) tobe printed to the output
    iso.turn_on_length()
    
    * turn off fields length to be printed
    iso.turn_off_length()
    
    * capture iso messages that come through stdin (default is 'json' the other one is 'iso') and output to stdout
    iso.stream()
    
    * stop streaming
    iso.stop_stream()

    +--------------------------+
    |         ISO FILE         |
    +--------------------------+
    * instantiate an instance of IsoFile, default version is 93
    iso = IsoFile("path_to_file")

    * change any field value of your choice
    iso.change_field(2, '9999999999999999')
    
    * remove any number of fields of your choice
    iso.remove_fields(3, 4)

    * append a field alomg with value
    iso.append_field(99, '11idugfhdisuo')
    
    * allow length of fields(if there is any) tobe printed to the output
    iso.turn_on_length()
    
    * turn off fields length to be printed
    iso.turn_off_length()

    * produce csv file from the iso
    csv_file = iso.to_csv()

    * produce iso file from the iso (might be useful for inspection of the iso)
    iso_file = iso.to_iso()

    * produce json file from the iso
    json_file = iso.to_json()
    '''