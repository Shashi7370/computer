import java.applet.*;
import java.awt.*;
public class MyApplet extends Applet
{
    public void init()
    {
	setBackground(Color.magenta);
    }
    public void paint(Graphics g)
    {
	g.drawString("India is a great country",100,200);
    }
}