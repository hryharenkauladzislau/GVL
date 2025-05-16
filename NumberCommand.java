public class NumberCommand implements Command {
    private Calculator calculator;
    private int number;

    public NumberCommand(Calculator calculator, int number) {
        this.calculator = calculator;
        this.number = number;
    }

    @Override
    public void execute() {
        calculator.setValue(calculator.getValue() * 10 + number);
    }
}