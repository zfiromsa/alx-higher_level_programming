#!/usr/bin/node

class Rectangle
{
    constuctor(w, h)
    {
        if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0)
        {
            this.width = w;
            this.height = h;
        }
        else
        {
            return {};
        }
    }
}

