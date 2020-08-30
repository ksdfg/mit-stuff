public class basics {
    public static void main(String[] args) {
        // string to play with
        String s = "hello world";
        System.out.println(s);

        // substring
        System.out.println("---\tSubstring\t---");
        String sub1 = s.substring(3);
        String sub2 = s.substring(3, 5);
        System.out.println("s: " + s + "\nsub1: " + sub1 + "\nsub2: " + sub2);

        // charAt
        System.out.println("---\tcharAt\t---");
        System.out.println("index\tcharacter");
        System.out.println(s.charAt(0) + "\t" + "0");
        System.out.println(s.charAt(5) + "\t" + "5");

        // equality checks
        System.out.println("---\tequality check\t---");
        String s2 = "hello world";
        String s3 = "bye world";
        System.out.println(s + "equal to " + s2 + " ? " + s.equals(s2));
        System.out.println(s + "equal to " + s3 + " ? " + s.equals(s3));

        // split
        System.out.println("---\tsplitting strings\t---");
        String names = "split, names, by, comma";
        String[] splitNames = names.split(",");
        for (String name : splitNames) {
            System.out.println(name);
        }

        // arrays
        System.out.println("---\tArrays\t---");
        int[] arr1;
        arr1 = new int[]{1, 2, 3};
        int[] arr2 = new int[]{4, 5, 6};
        int[] arr3 = {7, 8, 9};
        System.out.println("arr 1");
        for (int i : arr1) {
            System.out.println(i);
        }
        System.out.println("arr 2");
        for (int i : arr2) {
            System.out.println(i);
        }
        System.out.println("arr 3");
        for (int i : arr3) {
            System.out.println(i);
        }
    }
}