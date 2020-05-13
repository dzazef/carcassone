precision mediump float;

varying vec2 vTextureCoord;
uniform sampler2D uSampler;
uniform vec2 dimensions;
uniform vec4 filterArea;
uniform int tileDescription[49];
uniform int DEFAULT;
uniform int CASTLE;
uniform int MEADOW;
uniform int ROAD_END;
uniform int CASTLE_SHIELD;
uniform int ROAD;
uniform int MONASTERY;
float borderWidth = 0.005;

// przekształcenie canvasowych współrzędnych
// na współrzędne na spricie ((0,0) - lewy górny róg,
// (1,1) - prawy dolny róg)
vec2 normalizeCoord(vec2 coords) {
    vec2 pixelCoord = vTextureCoord * filterArea.xy;
    return pixelCoord / dimensions;
}

vec4 meadowColor() {
    return vec4(0.0, 0.5, 0.0, 1.0);
}

vec4 defaultColor() {
    return meadowColor();
}

vec4 castleColor() {
    return vec4(0.4, 0.2, 0.0, 1.0);
}

vec4 roadColor() {
    return vec4(0.4, 0.4, 0.4, 1.0);
}

vec4 monasteryColor() {
    return vec4(1.0, 0.6, 0.8, 1.0);
}

vec4 roadEndColor() {
    return vec4(0.0, 0.0, 0.0, 1.0);
}

// zwraca kolor, jaki odpowiada obszarowi
// o numerze areaNumber
vec4 getColor(int areaNumber) {
    if(areaNumber == DEFAULT) {
        return defaultColor();
    }
    if(areaNumber == MEADOW) {
        return meadowColor();
    }
    if(areaNumber == MONASTERY) {
        return monasteryColor();
    }
    if(areaNumber == ROAD) {
        return roadColor();
    }
    if(areaNumber == ROAD_END) {
        return roadEndColor();
    }
    if(areaNumber == CASTLE) {
        return castleColor();
    }
    // areaNumber == CASTLE_SHIELD
    return meadowColor();
}

int getAreaNumber(float x, float y) {
    for(int i = 0; i < 49; i++) {
        int row = i / 7;
        int column = i - row * 7;
        if(x < float(column + 1) / 7.0 && y < float(row + 1) / 7.0) {
            return tileDescription[i];
        }
    }
    return 0;
}

void main(void)
{
    // kolor piksela o współrzędnych (na canvasie!)
    // vTextureCoord na obrazie uSampler
    vec4 color = texture2D(uSampler, vTextureCoord);
    vec2 normalizedCoord = normalizeCoord(vTextureCoord);
    float x = normalizedCoord.x;
    float y = normalizedCoord.y;

    color = getColor(getAreaNumber(x, y));

    gl_FragColor = color;
}