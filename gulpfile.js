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
    rimraf = require('rimraf');

var path = {
    build: { // production
        js: 'consult_panel/static/main/js/',
        jsLib: 'consult_panel/static/main/js/lib/',
        css: 'consult_panel/static/main/css/',
        img: 'consult_panel/static/main/img/',
        fonts: 'consult_panel/static/main/fonts/'
    },
    src: { // development
        jsConsultPanel: 'consult_panel/static/main/src/js/consult-panel.js',
        jsPlugins: 'consult_panel/static/main/src/js/plugins.js',
        jsLib: 'consult_panel/static/main/src/js/lib/**/*.*',
        jsApp: 'consult_panel/static/main/src/js/app/app.js',
        styleTemplate: 'consult_panel/static/main/src/styles/template.less',
        styleLib: 'consult_panel/static/main/src/styles/libs.less',
        styleConsultPanel: 'consult_panel/static/main/src/styles/consult-panel.less',
        img: 'consult_panel/static/main/src/img/**/*.*',
        fonts: 'consult_panel/static/main/src/fonts/**/*.*'
    },
    watch: {
        jsConsultPanel: [
            'consult_panel/static/main/src/js/consult-panel.js',
            'consult_panel/static/main/src/js/consult-panel/**/*.js'
        ],
        jsPlugins: [
            'consult_panel/static/main/src/js/plugins.js',
            'consult_panel/static/main/src/js/vendor/**/*.js',
            'consult_panel/static/main/src/js/lib/**/*.js',
            'consult_panel/static/main/bower_components/**/*.js'
        ],
        styleTemplate: [
            'consult_panel/static/main/src/styles/template.less',
            'consult_panel/static/main/src/styles/vendor/**/*.less',
            'consult_panel/static/main/src/styles/partials/**/*.less',
            'consult_panel/static/main/src/styles/elements/**/*.less',
            'consult_panel/static/main/src/styles/pages/**/*.less'
        ],
        styleLib: [
            'consult_panel/static/main/src/styles/libs.less',
            'consult_panel/static/main/src/styles/lib/**/*.less'
        ],
        styleConsultPanel: [
            'consult_panel/static/main/src/styles/consult-panel.less',
            'consult_panel/static/main/src/styles/partials/vars.less',
            'consult_panel/static/main/src/styles/consult-panel/**/*.less'
        ]
    }
};

/* =====================================================
    JS
    ===================================================== */

gulp.task('jsConsultPanel:build', function () {
    return gulp.src(path.src.jsConsultPanel)
        .pipe(rigger())
        .pipe(uglify())
        .pipe(gulp.dest(path.build.js));
});

gulp.task('jsPlugins:build', function () {
    return gulp.src(path.src.jsPlugins)
        .pipe(rigger())
        .pipe(uglify())
        .pipe(gulp.dest(path.build.js));
});

gulp.task('jsLib:build', function () {
    return gulp.src(path.src.jsLib)
        .pipe(uglify())
        .pipe(gulp.dest(path.build.jsLib));
});

gulp.task('jsApp:build', function () {
    return gulp.src(path.src.jsApp)
        .pipe(rigger())
        .pipe(uglify())
        .pipe(gulp.dest(path.build.js));
});


/* =====================================================
    STYLES
    ===================================================== */

gulp.task('styleTemplate:build', function () {
    return gulp.src(path.src.styleTemplate)
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.css));
});

gulp.task('styleLib:build', function () {
    return gulp.src(path.src.styleLib)
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.css));
});

gulp.task('styleConsultPanel:build', function () {
    return gulp.src(path.src.styleConsultPanel)
        .pipe(less())
        .pipe(autoprefix({
            browsers: ['last 30 versions', '> 1%', 'ie 8', 'ie 9'],
            cascade: true
        }))
        .pipe(minifyCSS())
        .pipe(gulp.dest(path.build.css));
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
    'fonts:build',
    'jsConsultPanel:build',
    'jsPlugins:build',
    'jsLib:build',
    'jsApp:build',
    'styleTemplate:build',
    'styleLib:build',
    'styleConsultPanel:build',
    'image:build'
]);

gulp.task('front', [
    'jsConsultPanel:build',
    'jsPlugins:build',
    'jsLib:build',
    'js:build',
    'styleTemplate:build',
    'styleLib:build',
    'styleConsultPanel:build'
]);

gulp.task('js', [
    'jsConsultPanel:build',
    'jsPlugins:build',
    'jsLib:build',
    'jsApp:build'
]);

gulp.task('style', [
    'styleTemplate:build',
    'styleLib:build',
    'styleConsultPanel:build'
]);

gulp.task('media', [
    'fonts:build',
    'image:build'
]);

/* =====================================================
    WATCH
    ===================================================== */

gulp.task('watch', function(){
    watch(path.watch.jsConsultPanel, function(event, cb) {
        gulp.start('jsConsultPanel:build');
    });
    watch(path.watch.jsPlugins, function(event, cb) {
        gulp.start('jsPlugins:build');
    });
    watch([path.src.jsLib], function(event, cb) {
        gulp.start('jsLib:build');
    });
    watch([path.src.jsApp], function(event, cb) {
        gulp.start('jsApp:build');
    });
    watch(path.watch.styleTemplate, function(event, cb) {
        gulp.start('styleTemplate:build');
    });
    watch(path.watch.styleLib, function(event, cb) {
        gulp.start('styleLib:build');
    });
    watch(path.watch.styleConsultPanel, function(event, cb) {
        gulp.start('styleConsultPanel:build');
    });
    watch([path.src.img], function(event, cb) {
        gulp.start('image:build');
    });
    watch([path.src.fonts], function(event, cb) {
        gulp.start('fonts:build');
    });
});


/* =====================================================
    DEFAULT TASK
    ===================================================== */

/* gulp.task('default', ['build', 'webserver', 'watch']); */

gulp.task('default', ['build']);