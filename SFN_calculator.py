def hex_to_bin_str(hex_value, length):
    return format(int(hex_value, 16), f'0{length}b')

def decode_time(hex_time):
    # Convert to binary after reversing bytes for little-endian
    reversed_time = hex_time[2:] + hex_time[:2]
    bin_time = hex_to_bin_str(reversed_time, 16)
    # Extract components
    hour = int(bin_time[:5], 2)
    minute = int(bin_time[5:11], 2)
    second = int(bin_time[11:], 2) * 2
    return f"{hour:02}:{minute:02}:{second:02}"

def decode_date(hex_date):
    # Convert to binary after reversing bytes for little-endian
    reversed_date = hex_date[2:] + hex_date[:2]
    bin_date = hex_to_bin_str(reversed_date, 16)
    # Extract components
    year = (int(bin_date[:7], 2) + 1980)
    month = int(bin_date[7:11], 2)
    day = int(bin_date[11:], 2)
    return f"{year}-{month:02}-{day:02}"

def decode_attributes(hex_value):
    bin_value = hex_to_bin_str(hex_value, 8)
    if bin_value == "00100000":
        return "Archive"
    elif bin_value == "00001111":
        return "Long File Name"
    else:
        flags = {
            0x01: "Read-Only",
            0x02: "Hidden File",
            0x04: "System File",
            0x08: "Volume Label",
            0x10: "Directory",
            0x20: "Archive"
        }
        attributes = []
        for flag_hex, description in flags.items():
            if int(bin_value, 2) & flag_hex:
                attributes.append(description)
        return ", ".join(attributes)

def parse_hex_input(hex_input):
    # Split input based on the provided layout
    sfn_name = hex_input[:16]
    extension = hex_input[16:22]
    attributes = hex_input[22:24]
    reserved = hex_input[24:26]
    create_time_tenths = hex_input[26:28]
    creation_time = hex_input[28:32]
    creation_date = hex_input[32:36]
    last_accessed_date = hex_input[36:40]
    first_cluster_high = hex_input[40:44]
    last_mod_time = hex_input[44:48]
    last_mod_date = hex_input[48:52]
    first_cluster_low = hex_input[52:56]
    file_size = hex_input[56:]

    # Decode each field
    results = {
        "SFN Name(ASCII)": bytes.fromhex(sfn_name).decode(errors='replace'),
        "Extension": bytes.fromhex(extension).decode(errors='replace'),
        "Attributes": decode_attributes(attributes),
        "Reserved": reserved,
        "Create Time Tenths": create_time_tenths,
        "Creation Time": decode_time(creation_time),
        "Creation Date": decode_date(creation_date),
        "Last Date Accessed": decode_date(last_accessed_date),
        "First Cluster High": first_cluster_high,
        "Last Modification Time": decode_time(last_mod_time),
        "Last Modification Date": decode_date(last_mod_date),
        "First Cluster Low": first_cluster_low,
        "File Size (Bytes)": int(file_size[6:8] + file_size[4:6] + file_size[2:4] + file_size[0:2], 16)
    }

    return results

# Input
#Sample: 53595354454D7E31202020160042A50E714B714B0000A60E714B030000000000
#Sample: 544558542D4F7E314A5047200000436B714B714B0100EB4EFA4A58400C990200
hex_input = input("Enter the hex string: ").strip()

# Parse the hex input
parsed_data = parse_hex_input(hex_input)

# Output the results
for key, value in parsed_data.items():
    print(f"{key}: {value}")

