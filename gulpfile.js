'use strict';

var gulp = require('gulp'),
    watch = require('gulp-watch'),
    autoprefix = require('gulp-autoprefixer'),
    less = require('gulp-less'),
    minifyCSS = require('gulp-minify-css'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    gulpIgnore = require('gulp-ignore'),
    rigger = require('gulp-rigger'),
    imageop = require('gulp-image-optimization'),
    rimraf = require('rimraf'),
    browserSync = require("browser-sync"),
    reload = browserSync.reload;

var path = {
    build: { // production
        html: 'consult_panel/static/main/build/',
        js: 'consult_panel/static/main/build/js/',
        jsLib: 'consult_panel/static/main/build/js/lib/',
        css: 'consult_panel/static/main/build/css/',
        cssLib: 'consult_panel/static/main/build/css/lib/',
        img: 'consult_panel/static/main/build/img/',
        fonts: 'consult_panel/static/main/build/fonts/'
    },
    src: { // development
        html: '**/*.html',
        jsPlugins: 'consult_panel/static/main/js/plugins.js',
        jsLib: 'consult_panel/static/main/js/lib/**/*.*',
        js: 'consult_panel/static/main/js/app/app.js',
        style: 'consult_panel/static/main/styles/main.less',
        styleLib: 'consult_panel/static/main/styles/lib/*.css',
        styleLibFiles: 'consult_panel/static/main/styles/lib/**/*.*',
        styleLibIgnore: '!consult_panel/static/main/styles/lib/*.css',
        img: 'consult_panel/static/main/img/**/*.*',
        fonts: 'consult_panel/static/main/fonts/**/*.*'
    },
    watch: {
        html: 'consult_panel/static/main/**/*.html',
        js: 'consult_panel/static/main/js/**/*.js',
        style: 'consult_panel/static/main/styles/**/*.*',
        img: 'consult_panel/static/main/img/**/*.*',
        fonts: 'consult_panel/static/main/fonts/**/*.*'
    },
    clean: './consult_panel/static/main/build'
};

/* =====================================================
    SERVER
    ===================================================== */

var config = {
    server: {
        baseDir: "."
    },
    tunnel: true,
    host: 'localhost',
    port: 9000,
    logPrefix: "Frontend",
    watchTask: true
};

gulp.task('webserver', function () {
    browserSync(config);
});


/* =====================================================
    HTML
    ===================================================== */

gulp.task('html:build', function () {
    return gulp.src(path.src.html)
        .pipe(rigger())
        .pipe(gulp.dest(path.build.html))
        .pipe(reload({stream: true}));
});


/* =====================================================
    JS
    ===================================================== */

gulp.task('jsPlugins:build', function () {
    return gulp.src(path.src.jsPlugins)
        .pipe(rigger())
        .pipe(uglify())
        .pipe(gulp.dest(path.build.js))
        .pipe(reload({stream: true}));
});

gulp.task('jsLib:build', function () {
    return gulp.src(path.src.jsLib)
        //.pipe(uglify())
        .pipe(gulp.dest(path.build.jsLib))
        .pipe(reload({stream: true}));
});

gulp.task('js:build', function () {
    return gulp.src(path.src.js)
        .pipe(rigger())
        //.pipe(uglify())
        .pipe(gulp.dest(path.build.js))
        .pipe(reload({stream: true}));
});


/* =====================================================
    STYLES
    ===================================================== */

gulp.task('style:build', function () {
    return gulp.src(path.src.style)
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.css))
        .pipe(reload({stream: true}));
});

gulp.task('styleLib:build', function () {
    return gulp.src(path.src.styleLib)
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.cssLib))
        .pipe(reload({stream: true}));
});

gulp.task('styleLibFiles:build', function () {
    return gulp.src([path.src.styleLibFiles, path.src.styleLibIgnore])
        .pipe(gulp.dest(path.build.cssLib))

});


/* =====================================================
    IMAGES
    ===================================================== */

gulp.task('image:build', function (cb) {
    gulp.src(path.src.img)
        .pipe(imageop({
            optimizationLevel: 5,
            progressive: true,
            interlaced: true
        }))
        .pipe(gulp.dest(path.build.img)).on('end', cb).on('error', cb);
});


/* =====================================================
    FONTS
    ===================================================== */

gulp.task('fonts:build', function() {
    return gulp.src(path.src.fonts)
		.pipe(gulp.dest(path.build.fonts))
});


/* =====================================================
    BUILD TASK
    ===================================================== */

gulp.task('build', [
    //'html:build',
    'fonts:build',
    'jsPlugins:build',
    'jsLib:build',
    'js:build',
    'style:build',
    'styleLib:build',
    'styleLibFiles:build',
    'image:build'
]);


/* =====================================================
    WATCH
    ===================================================== */

gulp.task('watch', function(){
    watch([path.watch.html], function(event, cb) {
        gulp.start('html:build');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('style:build');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('styleLib:build');
    });
    watch([path.watch.style], function(event, cb) {
        gulp.start('styleLibFiles:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('jsPlugins:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('jsLib:build');
    });
    watch([path.watch.js], function(event, cb) {
        gulp.start('js:build');
    });
    watch([path.watch.img], function(event, cb) {
        gulp.start('image:build');
    });
    watch([path.watch.fonts], function(event, cb) {
        gulp.start('fonts:build');
    });
});


/* =====================================================
    CLEAN PRODUCTION
    ===================================================== */

gulp.task('clean', function (cb) {
    rimraf(path.clean, cb);
});


/* =====================================================
    DEFAULT TASK
    ===================================================== */

/* gulp.task('default', ['build', 'webserver', 'watch']); */

gulp.task('default', ['build']);