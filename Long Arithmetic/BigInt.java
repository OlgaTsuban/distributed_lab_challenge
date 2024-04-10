import java.math.BigInteger;

public class BigInt {
    private BigInteger value;

    // Constructors
    public BigInt(BigInteger value) {
        this.value = value;
    }

    public BigInt(long value) {
        this.value = BigInteger.valueOf(value);
    }

    public BigInt(String value) {
        this.value = new BigInteger(value);
    }

    // Arithmetic operations + - / * ** abc %
    public BigInt add(BigInt other) {
        return new BigInt(this.value.add(other.value));
    }

    public BigInt subtract(BigInt other) {
        return new BigInt(this.value.subtract(other.value));
    }

    public BigInt multiply(BigInt other) {
        return new BigInt(this.value.multiply(other.value));
    }

    public BigInt divide(BigInt other) {
        return new BigInt(this.value.divide(other.value));
    }

    public BigInt remainder(BigInt other) {
        return new BigInt(this.value.remainder(other.value));
    }

    public BigInt pow(int p) {
        BigInteger result = this.value.pow(p);
        return new BigInt(result);
    }

    public BigInt mod(BigInt other) {
        BigInteger result = this.value.mod(other.value);
        return new BigInt(result);
    }

    // Comparison operations <, <=, >, >= , ==
    public boolean lessThan(BigInt other) {
        return this.value.compareTo(other.value) < 0;
    }

    public boolean greaterThan(BigInt other) {
        return this.value.compareTo(other.value) > 0;
    }

    public boolean equalTo(BigInt other) {
        return this.value.equals(other.value);
    }

    public boolean lessThanOrEqual(BigInt o) {
        return this.value.equals(o.value) | this.lessThan(o);
    }

    public boolean greaterThanOrEqual(BigInt o) {
        return this.value.equals(o.value) | this.greaterThan(o);
    }

    // Conversion methods: from str to BigInt, from BigInt to str, From BigInt to Int
    public int toInt() {
        return this.value.intValue();
    }

    @Override
    public String toString() {
        return this.value.toString();
    }

    public static BigInteger parseStringToBigInt(String value) {
        value = value.trim();

        if (value.isEmpty()) {
            throw new NumberFormatException("Empty string cannot be converted to BigInt");
        }
        boolean isNegative = false;
        if (value.charAt(0) == '-') {
            isNegative = true;
            value = value.substring(1);
        } else if (value.charAt(0) == '+') {
            value = value.substring(1);
        }

        for (char c : value.toCharArray()) {
            if (!Character.isDigit(c)) {
                throw new NumberFormatException("Invalid characters in string: " + value);
            }
        }

        BigInteger bigInt = new BigInteger(value, 10);

        return isNegative ? bigInt.negate() : bigInt;
    }


    public static void main(String[] args) {
        BigInt a = new BigInt("123456789012345678901234567890");
        BigInt b = new BigInt("987654321098765432109876543210");

        // + - / % ** *
        BigInt sum = a.add(b);
        BigInt difference = a.subtract(b);
        BigInt product = a.multiply(b);
        BigInt quotient = a.divide(b);
        BigInt remainder = a.remainder(b);
        BigInt pow = a.pow(0);

        // <, <=, >=, >, ==
        boolean isALessThanB = a.lessThan(b);
        boolean isAGreaterThanB = a.greaterThan(b);
        boolean isAEqualToB = a.equalTo(b);
        boolean isALessEqualB = a.lessThanOrEqual(b);
        boolean isAGreaterEqualB = a.greaterThanOrEqual(b);
        
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Quotient: " + quotient);
        System.out.println("Remainder: " + remainder);
        System.out.println("Pow: " + pow);
        System.out.println("Is A less than B? " + isALessThanB);
        System.out.println("Is A greater than B? " + isAGreaterThanB);
        System.out.println("Is A equal to B? " + isAEqualToB);
        System.out.println("Is A equal or less than B? " + isALessEqualB);
        System.out.println("Is A equal or great to B? " + isAGreaterEqualB);

        System.out.println("To str: "+ a);
        System.out.println("To int: "+ a.toInt());
        System.out.println("From str: "+ parseStringToBigInt("123456789"));
    }
}
