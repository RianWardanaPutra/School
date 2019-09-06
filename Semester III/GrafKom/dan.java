public void drawLine(Graphics g) {
    float xinc, yinc, x, y;
    int steps, k;
    x = x1;
    y = y1;
    if (Math.abs(dx) > Math.abs(dy)) {
        steps = (int) Math.abs(dx);
    } else {
        steps = (int) Math.abs(dy);
    }
    xinc = (float) dx / (float) steps;
    yinc = (float) dy / (float) steps;
    g.drawLine(Math.round(x), Math.round(y), Math.round(x), Math.round(y));
    for (k = 0; k < steps; k++) {
        x = x + xinc;
        y = y + yinc;
        g.drawLine(Math.round(x), Math.round(y), Math.round(x), Math.round(y));
        try {
            Thread.sleep(10);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }
}

public void drawCircle1(Graphics g) {
    float t;
    float x, y, k;
    int centerX, centerY;
    k = 0;
    if (dx >= 0) {
        t = -(float) ((float) Math.atan(((float) dy / (float) dx)) - Math.PI / 2);
    } else {
        t = -(float) ((float) Math.atan(((float) dy / (float) dx)) + Math.PI / 2);
    }
    centerX = (int) (x1 - Math.round(r * Math.cos(t)));
    centerY = (int) (y1 + Math.round(r * Math.sin(t)));
    if (dx == 0 && dy == 0) {
        t = -(float) Math.atan(180);
        centerX = x1;
        centerY = y1 - r;
    }
    while (k <= 2 * Math.PI * r) {
        x = centerX + Math.round(r * Math.cos(t));
        y = centerY - Math.round(r * Math.sin(t));
        g.fillOval(Math.round(x), Math.round(y), 1, 1);
        t = t - (1 / (float) r);
        k++;
        try {
            Thread.sleep(10);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }
}