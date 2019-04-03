import math

R = 100
angle = 30
h = R * math.cos(angle / 180 * math.pi)
r = R * math.sin(angle / 180 * math.pi)

            # double x1 = r * hsv1.V * hsv1.S * Math.cos(hsv1.H / 180 * Math.PI);
            # double y1 = r * hsv1.V * hsv1.S * Math.sin(hsv1.H / 180 * Math.PI);
            # double z1 = h * (1 - hsv1.V);
            # double x2 = r * hsv2.V * hsv2.S * Math.cos(hsv2.H / 180 * Math.PI);
            # double y2 = r * hsv2.V * hsv2.S * Math.sin(hsv2.H / 180 * Math.PI);
            # double z2 = h * (1 - hsv2.V);
            # double dx = x1 - x2;
            # double dy = y1 - y2;
            # double dz = z1 - z2;
            # return Math.sqrt(dx * dx + dy * dy + dz * dz);
def _semblance(hsv1,hsv2):
    x1 = r * hsv1['V'] * hsv1['S'] * math.cos(hsv1['H'] / 180 * math.pi)
    y1 = r * hsv1['V'] * hsv1['S'] * math.sin(hsv1['H'] / 180 * math.pi)
    z1 = h * (1 - hsv1['V'])

    x2 = r * hsv2['V'] * hsv2['S'] * math.cos(hsv2['H'] / 180 * math.pi)
    y2 = r * hsv2['V'] * hsv2['S'] * math.sin(hsv2['H'] / 180 * math.pi)
    z2 = h * (1 - hsv2['V'])

    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2
    return math.sqrt(dx * dx + dy * dy + dz * dz)


