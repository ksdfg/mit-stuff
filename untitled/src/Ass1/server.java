package Ass1;

import Ass1.ProjectLibs.ServerTools;
import Ass1.ProjectLibs.Functions;

import java.util.Scanner;

public class server {

    public static void main(String[] args) {
        System.out.println("Enter shift value :");
        int shift = (new Scanner(System.in)).nextInt();

        try (ServerTools server = new ServerTools(8000)) {
            server.accept();
            System.out.println(Functions.decrypt(server.in.readUTF(), shift));
        }
        catch (Exception e) {
            System.out.println(e);
        }
    }

}
