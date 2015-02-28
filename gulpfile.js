
var gulp = require('gulp');
var jade = require('gulp-jade');
var stylus = require('gulp-stylus');

var outdir = 'django/nordostra/static/';

gulp.task('html', function() {
    return gulp.src('jade/*.jade')
                .pipe(jade())
                .pipe(gulp.dest(outdir + 'html'));
});

gulp.task('styles', function() {
    return gulp.src('stylus/*.styl')
        .pipe(stylus())
        .pipe(gulp.dest(outdir + 'styles'));
});

gulp.task('images', function() {
    return gulp.src('images/*').pipe(gulp.dest(outdir + "images"));
});

gulp.task('fonts', function() {
    return gulp.src('fonts/*').pipe(gulp.dest(outdir + "fonts"));
});

gulp.task('default', ['styles', 'html', 'images', 'fonts']);
