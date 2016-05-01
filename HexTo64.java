// Matasano Crypto Challenge
// Set      : 01
// Challenge: 01

// Convert hex to base64.
// The string: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
// Should produce: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

// Cryptopals Rule: Always operate on raw bytes, never on encoded strings. Only 
// use hex and base64 for pretty-printing. 

// Completed 2016/04/30

public class HexTo64 {
    public String hexTo64(String s) {
        String key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        
        // Guarantees multiple of 6.
        if (s.length() % 6 != 0) {
            for (int i = 0; i < s.length() % 6; i++) {
                s += "0";
            }
        }

        String decoded = new String();
        
        for (int i = 0; i < s.length(); i += 6) {
            String temp = s.substring(i, i+6);
            int b = Integer.parseInt(temp, 16);

            // Handling case of when the final 3 bytes only contain 1 or 2
            // bytes of data.
            if (temp.length() % 6 != 0) {
                if (6 - temp.length() == 2) {
                    b = b << 8;
                } else if (6 - temp.length() == 4) {
                    b = b << 16;
                }
            } 
            // Getting 6 bits at a time.
            int left = b >> 18;
            int mid_one = (b >> 12) & 0x3F;
            int mid_two = (b >> 6) & 0x3F;
            int last = b & 0x3F;

            // Building base64 string.
            decoded += key.charAt(left);
            decoded += key.charAt(mid_one);
            decoded += key.charAt(mid_two);
            decoded += key.charAt(last);
        }
        return decoded;
    }

    public static void main(String[] args) {
        HexTo64 h = new HexTo64();
        String a = h.hexTo64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
        System.out.println(a);
    }
}


