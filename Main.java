public class Main {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        Keyboard keyboard = new Keyboard();

        // Создаем кнопки
        Button button1 = new Button();
        button1.setCommand(new NumberCommand(calculator, 1));

        Button button2 = new Button();
        button2.setCommand(new NumberCommand(calculator, 2));

        Button addButton = new Button();
        addButton.setCommand(new ArithmeticCommand(calculator, "+", 5));

        Button customizableButton = new Button();
        CustomizableCommand customCmd = new CustomizableCommand();
        customizableButton.setCommand(customCmd);

        // Добавляем кнопки на клавиатуру
        keyboard.addButton(button1);
        keyboard.addButton(button2);
        keyboard.addButton(addButton);
        keyboard.addButton(customizableButton);

        // Используем калькулятор
        keyboard.pressButton(0); // Ввод 1
        keyboard.pressButton(1); // Ввод 2 (значение: 12)
        keyboard.pressButton(2); // +5 (значение: 17)

        // Переназначаем настраиваемую кнопку
        customCmd.setCommand(new ArithmeticCommand(calculator, "*", 2));
        keyboard.pressButton(3); // *2 (значение: 34)

        System.out.println("Результат: " + calculator.getValue());
    }
}