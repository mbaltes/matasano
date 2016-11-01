// Matasano Crypto Challenge
// Set      : 01
// Challenge: 03
//
// Single-byte XOR cipher
//
// The hex encoded string: 
// 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
//
//  ... has been XOR'd against a single character. Find the key, decrypt the 
//  message. You can do this by hand. But don't: write code to do it for you.
//
// How? Devise some method for "scoring" a piece of English plaintext. 
// Character frequency is a good metric. Evaluate each output and choose the 
// one with the best score. 
//
// Completed 

import java.util.*;

public class SingleXOR {
    // Return character with gretest frequency in a string.
    public static char charFreq(String s) {
        char topKey = '0';
        int topValue = 0;
        Map<Character, Integer> m = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (m.containsKey(c)) {
                m.put(c, m.get(c) + 1);
            } else {
                m.put(c, 1);
            }
        }
        for (Map.Entry<Character, Integer> entry : m.entrySet()) {
            int t = entry.getValue();
            if (t > topValue) {
                topKey = entry.getKey();
                topValue = t;
            }
        }
        return topKey;
    }

    // Main
    public static void main(String[] args) {
        String s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373"
                 + "e783a393b3736";
        // String s = "ETAOIN SHRDLU";
        // char top = charFreq(s);
        // String decoded = "";
        // System.out.println("Top: " + top);
        // decoded += s.charAt(0) ^ top;
        // System.out.println("decoded: " + decoded);
        // for (int i = 0; i < s.length(); i++) {
        //     decoded += s.charAt(i) ^ top;
        // }
        // System.out.println(decoded);
        int x = 0xb ^ 0x3;
        System.out.println(x);
    }
}