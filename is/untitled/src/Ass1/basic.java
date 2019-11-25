package Ass1;

import java.util.Random;
import java.util.Scanner;

public class basic {

    public static String encrypt (String text, char[] shuffle) {
        String result = "";

        for (int i=0; i<text.length(); i++){
            if(Character.isUpperCase(text.charAt(i))){
                result += Character.toUpperCase(shuffle[((int)text.charAt(i))-65]);
            } else {
                result += shuffle[((int)text.charAt(i))-97];
            }
        }

        return result;
    }

    public static String decrypt (String text, char[] shuffle) {
        String result = "";



        return result;
    }

    public static void main(String[] args) {

        char[] shuffle = new char[26];
        for (int i=97; i<122; i++)
            shuffle[i-97] = (char)i;
        System.out.println(new String(shuffle));

        Random r = new Random();
        char swap;
        int index;
        for (int i=0; i<26; i++){
            index = r.nextInt(26);
            System.out.println(shuffle[index]);
            swap = shuffle[i];
            shuffle[i] = shuffle[index];
            shuffle[index] = swap;
        }
        System.out.println(new String(shuffle));

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the string : ");
        String text = sc.next();

        System.out.println("Modified String : " + encrypt(text, shuffle));

    }

}
