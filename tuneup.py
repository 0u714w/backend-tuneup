#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "dougenas"

import cProfile
import pstats
import timeit



def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def profiler(*args, **kwargs):
            cp = cProfile.Profile()
            cp.enable()
            result = func(*args, **kwargs)
            cp.disable()
            sortby = 'cumulative'
            ps = pstats.Stats(cp).sort_stats(sortby)
            ps.print_stats()
            return result
    return profiler


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    time = t.repeat(repeat=7, number=3)
    print ("Minimum of Average Performances: {}".format(min(time) / 3))


def main():
    """Computes a list of duplicate movie entries"""

    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))



if __name__ == '__main__':
    main()
