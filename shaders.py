# Referencia del repo de Dennis

vertex_shader = """
layout (location = 0) in vec4 pos;
layout (location = 1) in vec4 normal;
layout (location = 2) in vec2 texcoords;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

uniform vec4 color;
uniform vec4 light;

out vec4 vertexColor;
out vec2 vertexTexcoords;

void main()
{
    float intensity = dot(model * normal, normalize(light - pos));

    gl_Position = projection * view * model * pos;
    vertexColor = color * intensity;
    vertexTexcoords = texcoords;
}
"""


fragment_shader = """
layout (location = 0) out vec4 diffuseColor;

in vec4 vertexColor;
in vec2 vertexTexcoords;

uniform sampler2D tex;

void main()
{
    diffuseColor =  vertexColor * texture(tex, vertexTexcoords);
}
"""