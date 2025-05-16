import java.util.ArrayList;
import java.util.List;

public class Keyboard {
    private List<Button> buttons = new ArrayList<>();

    public void addButton(Button button) {
        buttons.add(button);
    }

    public void pressButton(int index) {
        if (index >= 0 && index < buttons.size()) {
            buttons.get(index).press();
        }
    }
}