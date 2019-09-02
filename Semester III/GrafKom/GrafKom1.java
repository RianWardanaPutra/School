import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.BorderFactory;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.BevelBorder;

class Graf extends JFrame {

    Graf() {
        initComponents();
        setVisible(true);
    }

    public void initComponents() {
        panel = new Panel();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel.setBorder(BorderFactory.createBevelBorder(BevelBorder.RAISED));
        this.add(panel);
        pack();
    }

    class Panel extends JPanel {

        Panel() {
            setBackground(Color.GREEN);
            setPreferredSize(new Dimension(640, 640));
        }

        void drawLine(int xa, int ya, int xb, int yb) {
            double dx, dy, xinc, yinc, x, y;
            int steps, k;

            dx = xb - xa;
            dy = yb - ya;
        }

        @Override
        public void paint(Graphics g) {
            super.paint(g);
            g.drawArc(100, 100, 50, 50, 0, 360);
        }
    }

    private Panel panel;

    public static void main(String[] args) {
        Graf graf = new Graf();
    }
}