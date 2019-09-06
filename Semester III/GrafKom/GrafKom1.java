import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.BevelBorder;

class Graf extends JFrame {

    private static final long serialVersionUID = 1L;

	Graf() {
        initComponents();
    }

    public void initComponents() {
        panel = new Panel();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel.setBorder(BorderFactory.createBevelBorder(BevelBorder.RAISED));
        this.add(panel);
        pack();
    }

    class Panel extends JPanel implements Runnable{

        private static final long serialVersionUID = 1L;

        double xinc, yinc, x, y;
        int steps, k, dx, dy;

		Panel() {
            //setBackground(Color.GREEN);
            setPreferredSize(new Dimension(640, 640));
        }

        void drawLine(int xa, int ya, int xb, int yb) {

            dx = (xb - xa);
            dy = (yb - ya);
            x = (double)xa;
            y = (double)ya;
            if(dx>dy) {
                steps = dx;
            } else {
                steps = dy;
            }

            xinc = dx/steps;
            yinc = dy/steps;
            repaint(xa, ya, 1, 1);
            run();
            
        }

        @Override
        public void paint(Graphics g) {
            super.paint(g);
            g.drawArc(100, 100, 50, 50, 0, 360);
        }

		@Override
		public void run() {
			for(k = 0; k < steps; k++) {
                x += xinc;
                y += yinc;
                repaint((int)x, (int)y, 1, 1);
                try {
					wait(50);
        		} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
            }
		}
    }

    private Panel panel;

    public static void main(String[] args) {
        Graf graf = new Graf();
        graf.setVisible(true);
        graf.panel.drawLine(50, 50, 500, 500);
    }
}