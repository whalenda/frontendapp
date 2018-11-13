package com.gulogulo.starterapp;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;

public class PhotoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.found_photo);
        if(getIntent().hasExtra("byteArray")) {
            ImageView previewThumbnail = (ImageView) findViewById(R.id.image);
            Bitmap b = BitmapFactory.decodeByteArray(
                    getIntent().getByteArrayExtra("byteArray"),0,getIntent().getByteArrayExtra("byteArray").length);
            previewThumbnail.setImageBitmap(b);
        }
    }

    public void gotodone(View view)
    {
        Intent intent = new Intent(PhotoActivity.this, info.class);
        startActivity(intent);
    }
}
