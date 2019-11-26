package Ass1.ProjectLibs;

public class Functions {

    public static String encrypt (String text, int shift) {
        String result = "";

        for(int i=0; i<text.length(); i++){
            if(Character.isUpperCase(text.charAt(i))){
                result += (char) (((((int)text.charAt(i) - 65) + shift) % 26) + 65);
            } else {
                result += (char) (((((int)text.charAt(i) - 97) + shift) % 26) + 97);
            }
        }

        return result;
    }

    public static String decrypt (String text, int shift) {
        String result = "";

        for(int i=0; i<text.length(); i++){
            if(Character.isUpperCase(text.charAt(i))){
                result += (char) (((((int)text.charAt(i) - 65) - shift) % 26) + 65);
            } else {
                result += (char) (((((int)text.charAt(i) - 97) - shift) % 26) + 97);
            }
        }
        
        return result;
    }
}
