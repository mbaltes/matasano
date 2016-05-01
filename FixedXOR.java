// Matasano Crypto Challenge
// Set      : 01
// Challenge: 02

// Write a function that takes two equal-length buffers and produces their XOR 
// combination. If your function works properly, then when you feed it the 
// string: 1c0111001f010100061a024b53535009181c ... after hex decoding, and 
// when XOR'd against 686974207468652062756c6c277320657965 should produce:
// 746865206b696420646f6e277420706c6179 

// Completed 2016/05/01

public class FixedXOR {

    public static String fxor(String a, String b) {
        String produce = new String();
        for (int i = 0; i < a.length(); i++) {
            String tempLeft = a.substring(i, i+1);
            String tempRight = b.substring(i, i+1);

            int decodeLeft = Integer.parseInt(tempLeft, 16);
            int decodeRight = Integer.parseInt(tempRight, 16);

            Integer xor = decodeLeft ^ decodeRight;
            produce += Integer.toHexString(xor);
        }
        return produce;
    }

    public static void main(String[] args) {
        String x = fxor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965");
        System.out.println(x);
    }
}