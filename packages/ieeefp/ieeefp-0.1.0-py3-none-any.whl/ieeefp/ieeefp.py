import struct
import sys

def float_to_ieee754(value, bits):
    if bits == 32:
        packed = struct.pack('>f', value)  # Pack as big-endian float (4 bytes)
        hex_representation = f"0x{struct.unpack('>I', packed)[0]:08X}"  # Convert to hex
    elif bits == 64:
        packed = struct.pack('>d', value)  # Pack as big-endian double (8 bytes)
        hex_representation = f"0x{struct.unpack('>Q', packed)[0]:016X}"  # Convert to hex
    else:
        raise ValueError("Supported bit lengths are 32 and 64 only.")
    
    return hex_representation

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ieeefp.py <decimal_number> <bit_length> \n Example : python ieeefp.py -12.25 32 (for 32 bit version)")
        sys.exit(1)

    try:
        number = float(sys.argv[1])
        bit_length = int(sys.argv[2])

        if bit_length not in [32, 64]:
            raise ValueError

        ieee_hex = float_to_ieee754(number, bit_length)
        print(ieee_hex)

    except ValueError:
        print("Error: Please provide a valid decimal number and either 32 or 64 as bit length.")
        sys.exit(1)
