#!/usr/bin/env bash

# Compares two version numbers to tell you if you have a good version number
# Usage:    version_at_least CURRENT_VERSION REQUIRED_VERSION
# Arguments:
#           CURRENT_VERSION     The current version number of software (x.y.z)
#           REQUIRED_VERSION    The minimum required version number (x.y.z)
# Returns:
#           true                if CURRENT_VERSION >= REQUIRED_VERSION
#           false               if CURRENT_VERSION <  REQUIRED_VERSION
# Reference:
#           https://unix.stackexchange.com/a/285928/
function version_at_least() {
    local current_ver=$1
    local required_ver=$2

    local lesser_version="$(printf "${current_ver}\n${required_ver}" | sort -V | head -n1)"

    # If the current version matches the required version, then its okay.
    if [[ "$current_ver" == "$required_ver" ]]; then
        echo true

    # If the lesser of the two versions is the required version, then its okay.
    # This means that the greater of the two versions provided is the current
    # version number of the active software.
    elif [[ "$lesser_version" == "$required_ver" ]]; then
        echo true

    # Else, the lesser version is actually the current version of the software.
    # Then, we must return false because the current version is not high enough.
    else
        echo false
    fi
}
