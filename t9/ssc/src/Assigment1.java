import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.IOException;
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

    public static void main(String[] args) {
        Map<String, Operands> OPTAB = (new Operands()).getOpTable();
        LinkedHashMap<String, TableValue> symbol_table = new LinkedHashMap<>();
        LinkedHashMap<String, TableValue> literal_table = new LinkedHashMap<>();
        List<Integer> pool_table = new ArrayList<>();

        try {
            // Read code from file
            Scanner scanner = new Scanner(new FileReader("/home/ksdfg/stuff/code/mit-stuff/t9/ssc/src/code.txt"));

            while (scanner.hasNextLine()) {
                // TODO : Need to go through everything here
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
