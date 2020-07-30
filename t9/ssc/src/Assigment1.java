import java.io.*;
import java.util.*;

class Operands {
    String statement_class;
    String machine_code;

    public String getStatement_class() {
        return statement_class;
    }

    public String getMachine_code() {
        return machine_code;
    }

    public Operands createTuple(String statement_class, String machine_code) {
        Operands Operands = new Operands();
        Operands.statement_class = statement_class;
        Operands.machine_code = machine_code;
        return Operands;
    }

    public Map<String, Operands> getOpTable() {
        Map<String, Operands> op_table = new HashMap<>();
        op_table.put("STOP", createTuple("IS", "0"));
        op_table.put("ADD", createTuple("IS", "1"));
        op_table.put("SUB", createTuple("IS", "2"));
        op_table.put("MULT", createTuple("IS", "3"));
        op_table.put("MOVER", createTuple("IS", "4"));
        op_table.put("MOVEM", createTuple("IS", "5"));
        op_table.put("COMP", createTuple("IS", "6"));
        op_table.put("BC", createTuple("IS", "7"));
        op_table.put("DIV", createTuple("IS", "8"));
        op_table.put("READ", createTuple("IS", "9"));
        op_table.put("PRINT", createTuple("IS", "10"));
        op_table.put("DC", createTuple("DL", "1"));
        op_table.put("DS", createTuple("DL", "2"));
        op_table.put("START", createTuple("AD", "1"));
        op_table.put("END", createTuple("AD", "2"));
        op_table.put("ORIGIN", createTuple("AD", "3"));
        op_table.put("EQU", createTuple("AD", "4"));
        op_table.put("LTORG", createTuple("AD", "5"));
        op_table.put("AREG", createTuple("RG", "1"));
        op_table.put("BREG", createTuple("RG", "2"));
        op_table.put("CREG", createTuple("RG", "3"));
        op_table.put("EQ", createTuple("CC", "1"));
        op_table.put("LT", createTuple("CC", "2"));
        op_table.put("GT", createTuple("CC", "3"));
        op_table.put("LE", createTuple("CC", "4"));
        op_table.put("GE", createTuple("CC", "5"));
        op_table.put("NE", createTuple("CC", "6"));
        return op_table;
    }
}

class TableValue {
    int address;
    int index;

    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
}


public class Assigment1 {
    public static boolean isOpCode(String token) {
        return (new Operands()).getOpTable().containsKey(token);
    }

    public static boolean isNumeric(String str) {
        try {
            Double.parseDouble(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static void printTable(BufferedWriter bw, LinkedHashMap<String, TableValue> symbol_table) throws IOException {
        for (String key : symbol_table.keySet()) {
            bw.write(key + "\t" + symbol_table.get(key).getAddress() + "\t" + symbol_table.get(key).getIndex() + "\n");
        }
    }

    public static int setLiteralTable(int address, LinkedHashMap<String, TableValue> literal_table) {
        for (String key : literal_table.keySet()) {
            TableValue tabValueHolder = literal_table.get(key);
            if (tabValueHolder.getAddress() == 0) {
                tabValueHolder.setAddress(address);
                address++;
            }
        }

        return address;
    }

    public static String stringOfTuple(Operands tuple) {
        return "(" + tuple.getStatement_class() + "," + tuple.getMachine_code() + ") ";
    }

    public static void main(String[] args) {
        Map<String, Operands> OpTable = (new Operands()).getOpTable();

        LinkedHashMap<String, TableValue> symbol_table = new LinkedHashMap<>();
        LinkedHashMap<String, TableValue> literal_table = new LinkedHashMap<>();
        List<Integer> pool_table = new ArrayList<>();

        int symbol_table_pointer = 1;
        int literal_table_pointer = 1;
        int address_pointer = 0;
        int tokenCounter;

        ArrayList<String> intermediateCode = new ArrayList<>();
        StringBuilder intermediateLine = new StringBuilder();

        try {
            Scanner scanner = new Scanner(new FileReader("/home/ksdfg/stuff/code/mit-stuff/t9/ssc/src/code.txt"));

            while (scanner.hasNextLine()) {
                String[] tokens = scanner.nextLine().split(" ");

                if (address_pointer != 0) {
                    intermediateLine.append(address_pointer).append(") ");
                }

                tokenCounter = 0;
                for (int i = 0; i < tokens.length; i++) {
                    Operands opTuple;
                    String token = tokens[i];

                    if (isOpCode(token)) {

                        opTuple = OpTable.get(token);
                        switch (token) {
                            case "END" -> {
                                intermediateLine = new StringBuilder();
                                intermediateLine.append(stringOfTuple(OpTable.get(token)));
                                address_pointer = setLiteralTable(address_pointer, literal_table);
                                pool_table.add(literal_table_pointer);
                            }
                            case "LTORG" -> {
                                intermediateLine = new StringBuilder();
                                address_pointer = setLiteralTable(address_pointer, literal_table);
                                pool_table.add(literal_table_pointer);
                            }
                            case "START" -> {
                                address_pointer = Integer.parseInt(tokens[i + 1]) - 1;
                                intermediateLine.append("(C,").append(Integer.parseInt(tokens[i + 1])).append(") ");
                                i++;
                            }
                            case "ORIGIN" -> {
                                TableValue symbol_table_item = symbol_table.get(tokens[i + 1]);
                                address_pointer = symbol_table_item.getAddress();
                                i++;
                            }
                        }

                        if (opTuple.getStatement_class().equals("RG") || opTuple.getStatement_class().equals("CC")) {
                            intermediateLine.append("(").append(opTuple.getMachine_code()).append(") ");
                        } else {
                            intermediateLine.append(stringOfTuple(opTuple));
                        }

                    } else if (symbol_table.containsKey(token)) {

                        intermediateLine.append("(S,").append(symbol_table.get(token).getIndex()).append(") ");

                    } else if (tokenCounter == 0) {

                        TableValue symbol_table_item = new TableValue();
                        symbol_table_item.setAddress(address_pointer);
                        symbol_table_item.setIndex(symbol_table_pointer);
                        symbol_table.put(token, symbol_table_item);
                        symbol_table_pointer++;

                    } else if (isNumeric(token)) {

                        if (tokens[i - 1].equals("DS")) {
                            TableValue symbol_table_item = new TableValue();
                            symbol_table_item.setAddress(address_pointer);
                            symbol_table_item.setIndex(symbol_table.get(tokens[i - 2]).getIndex());
                            symbol_table.put(tokens[i - 2], symbol_table_item);
                        } else if (tokens[i - 1].equals("DC")) {
                            TableValue symbol_table_item = new TableValue();
                            symbol_table_item.setAddress(address_pointer);
                            symbol_table_item.setIndex(symbol_table.get(tokens[i - 2]).getIndex());
                            symbol_table.put(tokens[i - 2], symbol_table_item);
                        }

                        intermediateLine.append("(C,").append(token).append(") ");

                    } else {

                        if (token.startsWith("=")) {
                            TableValue littabHolder = new TableValue();
                            littabHolder.setIndex(literal_table_pointer);
                            intermediateLine.append("(L,").append(literal_table_pointer).append(") ");
                            literal_table_pointer++;
                            literal_table.put(token, littabHolder);
                        } else {
                            TableValue symbol_table_item = new TableValue();
                            symbol_table_item.setAddress(-1);
                            symbol_table_item.setIndex(symbol_table_pointer);
                            symbol_table.put(token, symbol_table_item);
                            intermediateLine.append("(S,").append(String.valueOf(symbol_table_pointer)).append(") ");
                            symbol_table_pointer++;
                        }

                    }

                    tokenCounter++;
                }

                address_pointer++;
                intermediateCode.add(intermediateLine.toString());
                intermediateLine = new StringBuilder();
            }
        } catch (IOException e) {
            System.out.println("Input file not found");
            e.printStackTrace();
        }

        try {
            File out = new File("/home/ksdfg/stuff/code/mit-stuff/t9/ssc/src/output.txt");
            FileOutputStream fos = new FileOutputStream(out);
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));

            for (String line : intermediateCode) {
                bw.write(line + "\n");
            }

            bw.write("\nSYMBOL TABLE: \n");
            printTable(bw, symbol_table);

            bw.write("\nLITERAL TABLE: \n");
            printTable(bw, literal_table);

            bw.write("\npool_table:\n");
            for (int i : pool_table) {
                bw.write(i + "\n");
            }

            bw.close();
        } catch (IOException e) {
            System.out.println("Output file not found");
            e.printStackTrace();
        }
    }
}
