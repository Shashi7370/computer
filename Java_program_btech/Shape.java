import java.applet.*;
import java.awt.*;
public class Shape extends Applet
{         
        public void init()
        {	
	setBackground(Color.magenta);
        }
        public void paint(Graphics g)
        { 
	g.drawOval(200,80,200,50);
	g.drawLine(200,100,300,500);
	g.drawLine(400,100,300,500);

	g.drawOval(500,60,200,50);
	g.drawLine(500,80,500,300);
	g.drawLine(700,80,700,300);
	g.drawOval(500,280,200,50);

	g.drawRect(600,350,150,150);
	g.drawRect(675,425,150,150);
	g.drawLine(600,350,675,425);
	g.drawLine(750,500,825,575);
	g.drawLine(600,500,675,575);
	g.drawLine(750,350,825,425);

	g.drawRect(800,100,200,200);
	g.drawArc(850,150,100,100,0,360);

	g.drawArc(1050,100,200,200,0,360);
	g.drawRect(1100,150,100,100);
         }
}