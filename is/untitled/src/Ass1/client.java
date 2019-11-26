package Ass1;

import Ass1.ProjectLibs.ClientTools;
import Ass1.ProjectLibs.Functions;

import java.util.Scanner;

public class client {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter shift value :");
        int shift = sc.nextInt();
        System.out.println("Enter text to send :");
        String text = sc.next();

        try (ClientTools client = new ClientTools("localhost",8000)) {
            client.out.writeUTF(Functions.encrypt(text, shift));
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }

}
