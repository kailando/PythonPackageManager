"""Versioning for PPM
Versions are just one number
MUST be increasing, never decreases
Version spec format:
package==version: Package is EXACTLY version
package<=version: Package is less than or equal to version
package=<version: Same as <=
package>=version: Package is less than or equal to version
package=>version: Same as >=
package<<version: Package is less than version
package>>version: Package is greater than version
"""

class VersionError(ValueError):
    """An error with the version of a package."""
    pass

class VersionSpecError(VersionError):
    """An error with the spec of a version comparison."""
    pass

def _check(a,b,c):
    match c:
        case "=":
            return a==b
        case ">":
            return a>b
        case "<":
            return a<b
        case _:
            raise VersionSpecError(f"Invalid character: {c}")

def check(a: int, b: int, spec: str) -> bool:
    """Parse and check a version
a: The package's version
b: The wanted version
spec: The two-character comparison
"""
    if len(spec) != 2:
        raise VersionSpecError(f"Invalid version spec: {spec}")
    if spec[0]==spec[1]:
        return _check(a,b,spec[0])
    return _check(a,b,spec[0]) or _check(a,b,spec[1])
