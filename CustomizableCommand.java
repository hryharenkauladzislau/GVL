public class CustomizableCommand implements Command {
    private Command command;

    public void setCommand(Command command) {
        this.command = command;
    }

    @Override
    public void execute() {
        if (command != null) {
            command.execute();
        }
    }
}