public class ArithmeticCommand implements Command {
    private Calculator calculator;
    private String operator;
    private double operand;

    public ArithmeticCommand(Calculator calculator, String operator, double operand) {
        this.calculator = calculator;
        this.operator = operator;
        this.operand = operand;
    }

    @Override
    public void execute() {
        switch (operator) {
            case "+": calculator.setValue(calculator.getValue() + operand); break;
            case "-": calculator.setValue(calculator.getValue() - operand); break;
            case "*": calculator.setValue(calculator.getValue() * operand); break;
            case "/":
                if (operand != 0) {
                    calculator.setValue(calculator.getValue() / operand);
                }
                break;
        }
    }
}