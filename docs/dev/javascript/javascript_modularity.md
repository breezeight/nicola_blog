
# Modularity in JS

In JS we achive modularity with:

1. **Modularity in JavaScript**: Achieving modularity through modules, prototypes, and classes.

2. **Prototype**: Definition and references to resources on prototypes and inheritance.

3. **CheatSheet and TL;DR**: Key characteristics of objects and functions regarding prototypes.

4. **Object's Prototype**: Explanation of the `[[Prototype]]` property and methods for getting and setting prototypes.

5. **Prototypal Inheritance**: How inheritance works in JavaScript, including examples of prototype chains.

6. **This and Prototype**: Understanding the value of `this` in methods and inherited properties.

7. **Setting & Shadowing Properties**: Behavior of property assignments and shadowing in prototypes.

8. **Constructor Function**: Role of constructor functions and their prototype properties.

9. **Approximate Private Variables**: Using closures and prototypes to manage private variables.

10. **Example Problems**: Issues with prototype references and how to avoid them.

11. **Instanceof and Constructor Property**: Using `instanceof` to check prototype chains and constructor references.

12. **Writing Doesn’t Use Prototype**: How property assignments work directly with objects.

13. **Advanced Topics**: Discussion on the `for..in` loop and deprecated `__proto__` property.

14. **Inheritance**: Setting up prototype chains for inheritance and the importance of `Object.create`.

15. **Classes**: Introduction to ES6 classes as syntactic sugar over prototypes and their features.


## Prototype

Ref:

- [JSINFO](https://javascript.info/prototypes)
- [MDN Object prototypes - Basic](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes)
- [MDN Advanced](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain#Using_prototypes_in_JavaScript)
- [YDKJSY: this & Object Prototypes](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md)
- [JSFIP Prototype chains](https://exploringjs.com/impatient-js/ch_proto-chains-classes.html#prototype-chains)
- [FreeCodeCamp Prototype intro](https://www.freecodecamp.org/news/a-guide-to-prototype-based-class-inheritance-in-javascript-84953db26df0/)

### CheatSheet and TL;DR

Def: A prototype is an object to which the search for a particular property can be delegated to.

TODO elencare tutti i modi di usare la prototype inheritance

EVERY OBJECT:

- has a constructor property
- has a prototype that is either null or an object
- can have "own properties" (Non-inherited properties)
- if an object doesn't have a property JS looks up in the object prototype

ONLY FUNCTIONS:

- have a prototype property
- Object.setPrototypeOf (obj.\_\_proto=... is deprecated)
- Object.create(proto[, descriptors]) – creates an empty object with given proto as [[Prototype]] and optional property descriptors.
- Classes are syntactical sugar over JS https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes

WARNIGN: It's important to understand that there is a distinction between an object's prototype (available via Object.getPrototypeOf(obj), or via the deprecated **proto** property) and the prototype property on constructor functions. The former is the property on each instance, and the latter is the property on the constructor. That is, Object.getPrototypeOf(new Foobar()) refers to the same object as Foobar.prototype.

### Intro

In programming, we often want to take something and extend it.

A prototype is an object to which the search for a particular property can be delegated to. Prototypes serve a similar purpose to that of classes in classical object-oriented languages.

For instance, we have a user object with its properties and methods, and want to make admin and guest as slightly modified variants of it. We’d like to reuse what we have in user, not copy/reimplement its methods, just build a new object on top of it.

JavaScript objects use prototype-based inheritance. Its design is logically similar (but different in implementation) from class inheritance in strictly Object Oriented Programming languages.

It can be loosely described by saying that when methods or properties are attached to object’s prototype they become available for use on that object and its descendants. But this process often takes place behind the scenes.

When writing code, you will not even need to touch the `prototype` property directly. When executing the `split` method, you would call it directly from a string literal as: `”hello”.split(“e”)` or from a variable: `string.split(“,”)`;

When you use class and extends keywords internally JavaScript will still use prototype-based inheritance. It just simplifies the syntax. Perhaps this is why it’s important to understand how prototype-based inheritance works. It’s still at the core of the language design.

This is why in many tutorials you will see String.prototype.split written instead of just String.split. This means that there is a method split that can be used with objects of type string because it is attached to that object’s prototype property.

Note: ES6 Proxies are outside of our discussion scope in this section, but everything we discuss here about normal [[Get]] and [[Put]] behavior does not apply if a Proxy is involved.

### Object's prototype

Prototypal inheritance is a language feature that helps in that.

`[[Prototype]`: In JavaScript, every objects have a special hidden property `[[Prototype]]` (as named in the specification), that is either null or references another object. That object is called “a prototype”.

This property is HIDDEN, to manipulate it we use:

- Object.getPrototypeOf
- Object.setPrototypeOf

GET

- `myObject.__proto__` **DEPRECATED**
- `Object.getPrototypeOf(obj: Object) : Object`

SET

- `myObject.__proto__ = ....` **DEPRECATED**
- `Object.create(proto: Object, [propertiesObject: Object]) : Object` (BEST way when you create an object)
  - prepertiesObjects: property descriptors to be added
- `Object.setPrototypeOf`
- the `new` operator

Ref: [MDN Object.create](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

The prototype is a little bit “magical”. When we want to read a property from object, and it’s missing, JavaScript automatically takes it from the prototype. In programming, such thing is called “prototypal inheritance”. Many cool language features and programming techniques are based on it.

```js
let animal = {
  eats: true,
};
let rabbit = {
  jumps: true,
};

rabbit.__proto__ = animal; // (*)

// we can find both properties in rabbit now:
alert(rabbit.eats); // true (**)
alert(rabbit.jumps); // true
```

If we later add a method to animal rabbit will inherit it:

```js
animal.walk = function () {
  alert("Animal walk");
};
rabbit.walk();
```

The prototype chain can be longer:

```js
let animal = {
  eats: true,
  walk() {
    alert("Animal walk");
  },
};

let rabbit = {
  jumps: true,
  __proto__: animal,
};

let longEar = {
  earLength: 10,
  __proto__: rabbit,
};

// walk is taken from the prototype chain
longEar.walk(); // Animal walk
alert(longEar.jumps); // true (from rabbit)
```

what happens is:

- The js engine initially checks to see if the longEar object has a walk() method available on it and it doesn't.
- So the js engine checks to see if the longEar's prototype object has a walk() method available on it.
- It doesn't, then the browser checks rabbit's prototype object's prototype object, and it has. So the method is called, and all is good!

![](../images/js_prototype_long_chain.png)

There are only two limitations:

- The references can’t go in circles. JavaScript will throw an error if we try to assign **proto** in a circle.
- The value of **proto** can be either an object or null. Other types are ignored.
- Also it may be obvious, but still: there can be only one [[Prototype]]. An object may not inherit from two others.

Given that a prototype object can have a prototype itself, we get a chain of objects – the so-called `prototype chain`.

![](../images/js_prototype_chain.svg)

Prototypes are JavaScript’s only inheritance mechanism: each object has a prototype that is either null or an object.

### This and Prototype

REF: https://javascript.info/prototype-inheritance#the-value-of-this

```js
let user = {
  name: "John",
  surname: "Smith",

  set fullName(value) {
    [this.name, this.surname] = value.split(" ");
  },

  get fullName() {
    return `${this.name} ${this.surname}`;
  },
};

let admin = {
  __proto__: user,
  isAdmin: true,
};

alert(admin.fullName); // John Smith (*)

// setter triggers!
admin.fullName = "Alice Cooper"; // (**)
```

### Setting & Shadowing Properties. Inherited Setters

Refs:

- https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md#setting--shadowing-properties
- https://javascript.info/prototype-inheritance#writing-doesn-t-use-prototype

An interesting question may arise in the example above: what’s the value of this inside `set fullName(value)`? Where are the properties `this.name` and `this.surname` written: into user or admin?

The answer is simple: this is not affected by prototypes at all.

No matter where the method is found: in an object or its prototype. In a method call, this is always the object before the dot.

So, the setter call admin.fullName= uses admin as this, not user.

That is actually a super-important thing, because we may have a big object with many methods, and have objects that inherit from it. And when the inheriting objects run the inherited methods, they will modify only their own states, not the state of the big object.

For instance, here animal represents a “method storage”, and rabbit makes use of it.

The call rabbit.sleep() sets this.isSleeping on the rabbit object:

```js
// animal has methods
let animal = {
  walk() {
    if (!this.isSleeping) {
      alert(`I walk`);
    }
  },
  sleep() {
    this.isSleeping = true;
  },
};

let rabbit = {
  name: "White Rabbit",
  __proto__: animal,
};

// modifies rabbit.isSleeping
rabbit.sleep();

alert(rabbit.isSleeping); // true
alert(animal.isSleeping); // undefined (no such property in the prototype)
```

If we had other objects, like bird, snake, etc., inheriting from animal, they would also gain access to methods of animal. But this in each method call would be the corresponding object, evaluated at the call-time (before dot), not animal. So when we write data into this, it is stored into these objects.

As a result, methods are shared, but the object state is not.

### More on setting a property

We will now revisit this situation more completely.

```
myObject.foo = "bar";
```

If the myObject object already has a normal data accessor property called foo directly present on it, the assignment is as simple as changing the value of the existing property.

If foo is not already present directly on myObject, the [[Prototype]] chain is traversed, just like for the [[Get]] operation. If foo is not found anywhere in the chain, the property foo is added directly to myObject with the specified value, as expected.

However, if foo is already present somewhere higher in the chain, nuanced (and perhaps surprising) behavior can occur with the myObject.foo = "bar" assignment. We'll examine that more in just a moment.

If the property name foo ends up both on myObject itself and at a higher level of the [[Prototype]] chain that starts at myObject, this is called shadowing. The foo property directly on myObject shadows any foo property which appears higher in the chain, because the myObject.foo look-up would always find the foo property that's lowest in the chain.

As we just hinted, shadowing foo on myObject is not as simple as it may seem. We will now examine three scenarios for the myObject.foo = "bar" assignment when foo is not already on myObject directly, but is at a higher level of myObject's [[Prototype]] chain:

1. If a normal data accessor (see Chapter 3) property named foo is found anywhere higher on the [[Prototype]] chain, and it's not marked as read-only (writable:false) then a new property called foo is added directly to myObject, resulting in a shadowed property.
2. If a foo is found higher on the [[Prototype]] chain, but it's marked as read-only (writable:false), then both the setting of that existing property as well as the creation of the shadowed property on myObject are disallowed. If the code is running in strict mode, an error will be thrown. Otherwise, the setting of the property value will silently be ignored. Either way, no shadowing occurs.
3. If a foo is found higher on the [[Prototype]] chain and it's a setter (see Chapter 3), then the setter will always be called. No foo will be added to (aka, shadowed on) myObject, nor will the foo setter be redefined.
   Most developers assume that assignment of a property ([[Put]]) will always result in shadowing if the property already exists higher on the [[Prototype]] chain, but as you can see, that's only true in one (#1) of the three situations just described.

If you want to shadow foo in cases #2 and #3, you cannot use = assignment, but must instead use Object.defineProperty(..) (see Chapter 3) to add foo to myObject.

Note: Case #2 may be the most surprising of the three. The presence of a read-only property prevents a property of the same name being implicitly created (shadowed) at a lower level of a [[Prototype]] chain. The reason for this restriction is primarily to reinforce the illusion of class-inherited properties. If you think of the foo at a higher level of the chain as having been inherited (copied down) to myObject, then it makes sense to enforce the non-writable nature of that foo property on myObject. If you however separate the illusion from the fact, and recognize that no such inheritance copying actually occurred (see Chapters 4 and 5), it's a little unnatural that myObject would be prevented from having a foo property just because some other object had a non-writable foo on it. It's even stranger that this restriction only applies to = assignment, but is not enforced when using Object.defineProperty(..).

Shadowing with methods leads to ugly explicit pseudo-polymorphism (see Chapter 4) if you need to delegate between them. Usually, shadowing is more complicated and nuanced than it's worth, so you should try to avoid it if possible. See Chapter 6 for an alternative design pattern, which among other things discourages shadowing in favor of cleaner alternatives.

Shadowing can even occur implicitly in subtle ways, so care must be taken if trying to avoid it. Consider:

```js
var anotherObject = {
  a: 2,
};

var myObject = Object.create(anotherObject);

anotherObject.a; // 2
myObject.a; // 2

anotherObject.hasOwnProperty("a"); // true
myObject.hasOwnProperty("a"); // false

myObject.a++; // oops, implicit shadowing!

anotherObject.a; // 2
myObject.a; // 3

myObject.hasOwnProperty("a"); // true
```

Though it may appear that `myObject.a++` should (via delegation) look-up and just increment the anotherObject.a property itself in place, instead the ++ operation corresponds to `myObject.a = myObject.a + 1`. The result is [[Get]] looking up a property via [[Prototype]] to get the current value 2 from `anotherObject.a`, incrementing the value by one, then [[Put]] assigning the 3 value to a new shadowed property a on myObject. Oops!

Be very careful when dealing with delegated properties that you modify. If you wanted to increment `anotherObject.a`, the only proper way is `anotherObject.a++`.

### Constructor Function

All functions have a prototype property that initially references an empty object:

- This property doesn’t serve much purpose until the function is used as a constructor (using the `new` operator).
- this empty object's prototype is `Object.prototype`, so it inherits from Object
- The prototype object initially has only one property, `constructor`, that references back to the function (we will see how it is used)

```js
function f() {}
Object.getPrototypeOf(f.prototype) === Object.prototype;
```

NOTE:

- It's important to understand that there is a distinction between an object's prototype (available via `Object.getPrototypeOf(obj)`, or via the deprecated `__proto__` property) and the prototype property on constructor functions.
- The former is the property on each instance, and the latter is the property on the constructor. That is, Object.getPrototypeOf(new Foobar()) refers to the same object as Foobar.prototype.
- REF: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

Now we will see how JS use the function prototype property to create and initialize an object.

For example we define a seemingly donothing function named `Ninja` that we’ll invoke in two ways:

- as a “normal” function, const ninja1 = Ninja();
- and as a constructor, const ninja2 = new Ninja();.

```js
function Ninja() {}
Ninja.prototype.swingSword = function () {
  return true;
};

const ninja1 = Ninja();

//As expected a function without an explicit return statement, returns undefined
assert(ninja1 === undefined, "No instance of Ninja created.");

// With new something different happen, it return an object
const ninja2 = new Ninja();
assert(
  ninja2 && ninja2.swingSword && ninja2.swingSword(),
  "Instance exists and method is callable."
);

//Ninja.prototype is the ninja2 prototype object
Object.getPrototypeOf(ninja2) === Ninja.prototype;

// ninja2 and ninja3 have the same prototype
const ninja3 = new Ninja();
Object.getPrototypeOf(ninja2) === Object.getPrototypeOf(ninja3);
```

When we call the function via the new operator, invoking it as a constructor, and something completely different happens:

- The function is once again called, but this time a newly allocated object has been created
- and it is set as the context of the function (and is accessible through the this keyword).
- The result returned from the new operator is a reference to this new object
- that object has a `swingSword` method that we can call
- the prototype of the newly constructed object is set to the object referenced by the constructor function’s prototype property.

Notice that all objects created with the Ninja constructor will have access to the swingSword method. Now that’s code reuse!

![](../images/js_prototype_ninja.png)

IMPORTANT:

- The prototype property is one of the most confusingly-named parts of JavaScript — you might think that this points to the prototype object of the current object, but it doesn't (that's an internal object that can be accessed by `__proto__`, remember?). prototype instead is a property containing an object on which you define members that you want to be inherited.
- Ref: https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

### Approximate private variables with closures and Prototype

### Example and problems with prototype and references

Ref: https://medium.com/better-programming/prototypes-in-javascript-5bba2990e04b

```js
//Create an empty constructor function
function Person() {}
//Add property name, age to the prototype property of the Person constructor function
Person.prototype.name = "Ashwin";
Person.prototype.age = 26;
//Arrays are of reference type in JavaScript
Person.prototype.friends = ["Jadeja", "Vijay"];
Person.prototype.sayName = function () {
  console.log(this.name);
};

//Create an object using the Person constructor function
var person1 = new Person();

//Access the name property using the person object
console.log(person1.name); // Output" Ashwin

var person2 = new Person();
//Access the name property using the person2 object
console.log(person2.name); // Output: Ashwin

//Now, let’s define a property name on the person1 object
person1.name = "Anil";
console.log(person1.name); //Output: Anil
console.log(person2.name); //Output: Ashwin
```

- Here person1.name outputs “Anil”. As mentioned earlier, the JavaScript engine first tries to find the property on the object itself. In this case, name property is present on the object person1 itself, hence JavaScript engines outputs the value of name property of person1.
- In the case of person2, the name property is not present on the object. Hence, it outputs person2’s prototype object’s property name.

The code above is doing what we expect but let's see what happen if we try to change person1.friend array:

```js
//Add a new element to the friends array
person1.friends.push("Amit");

console.log(person1.friends); // Output: "Jadeja, Vijay, Amit"
console.log(person2.friends); // Output: "Jadeja, Vijay, Amit"
```

PROBLEM: we are changing also person2's friends! This happens because we are referncing the same array from the prototype. We are not setting a new property as with `name` we are updating the same array.

To solve the problems with the prototype and the problems with the constructor, we can combine both the constructor and function:

- Problem with the constructor function: Every object has its own instance of the function
- Problem with the prototype: Modifying a property using one object reflects the other object also

To solve both problems, we can define all the object-specific properties inside the constructor and all shared properties and methods inside the prototype as shown below:

```js
//Define the object specific properties inside the constructor
function Human(name, age) {
  (this.name = name), (this.age = age), (this.friends = ["Jadeja", "Vijay"]);
}
//Define the shared properties and methods using the prototype
Human.prototype.sayName = function () {
  console.log(this.name);
};
//Create two objects using the Human constructor function
var person1 = new Human("Virat", 31);
var person2 = new Human("Sachin", 40);

//Lets check if person1 and person2 have points to the same instance of the sayName function
console.log(person1.sayName === person2.sayName); // true

//Let's modify friends property and check
person1.friends.push("Amit");

console.log(person1.friends); // Output: "Jadeja, Vijay, Amit"
console.log(person2.friends); //Output: "Jadeja, Vijay"
```

Here as we have wanted each object to have their own name, age, and friends property. Hence, we have defined these properties inside the constructor using this. However, as sayName is defined on the prototype object, it will be shared among all the objects.
In the above example, the friend’s property of person2 did not change on changing the friends' property of person1.

![](../images/js_prototype_example1.png)

### Example: Problem when you replace a prototype

You can change the reference to a function's prototype but it can cause strange behaviours if you already create some object with that function: you could end up with objects created with the same function that behaves differently (see example below).

The reference between an object and the function’s prototype is established at
the time of object instantiation. Newly created objects will have a reference to the new prototype and will have access to the pierce method, whereas the old, pre-prototype-change objects keep their original prototype, happily swinging their swords.

```js
function Ninja() {
  this.swung = true;
}
const ninja1 = new Ninja();

// !! Change the constructor function prototype
Ninja.prototype.swingSword = function () {
  return this.swung;
};

Ninja.prototype = {
  pierce: function () {
    return true;
  },
};

const ninja2 = new Ninja();

//
ninja1.pierce(); // Uncaught TypeError: ninja1.pierce is not a function
ninja2.pierce(); //true
```

![](../images/js_redefine_prototype.png)

### instanceof and Constructor property

REF: [SOJSN2ND] 7.3.2 The instanceof operator

`instanceof` operator checks whether the prototype of the argument function is in the prototype chain of the object.

```js
function Person() {}
function Admin() {}
Admin.prototype = new Person();
admin = new Admin();
admin instanceof Person; // true
```

![](../images/js_instance_of_example.png)

```js
> [] instanceof Array
true
> 2 instanceof Array
false
```

THE INSTANCEOF CAVEAT: if we change the prototype of Admin the result is false:

```js
function Person() {}
function Admin() {}
Admin.prototype = new Person();
admin = new Admin();
admin instanceof Person; // true

Admin.prototype = {};
admin2 = new Admin();
admin2 instanceof Person; // false
```

This will surprise us only if we cling to the inaccurate assumption that the instanceof operator tells us whether an instance was created by a particular function constructor. If, on the other hand, we take the real semantics of the instanceof operator—that it checks only whether the prototype of the function on the right side is in the prototype chain of the object on the left side—we won’t be surprised.

NOTE: Many developer belive that each object in JavaScript has an implicit property named `constructor` that references the constructor function that was used to create the object. And because the prototype is a property of the constructor, each object has a way to find its prototype.

This behavior is quite standard but is not reliable.
`.constructor` is extremely unreliable, and an unsafe reference to rely upon in your code.

- [REF](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md#mechanics)

For example:

```js
function Foo() {
  /* .. */
}

Foo.prototype = {
  /* .. */
}; // create a new prototype object

var a1 = new Foo();
a1.constructor === Foo; // false!
a1.constructor === Object; // true!
```

Especially when you create multiple level of prototypal inheritance:

- [REF](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/this%20%26%20object%20prototypes/ch5.md#constructor-redux)

**NOTE**: _ONLY functions_ have a prototype property, _EVERY object_ has a
costructor property!

### Writing doesn’t use prototype

The prototype is only used for reading properties.

Write/delete operations work directly with the object.

In the example below, we assign its own walk method to rabbit:

```js
let animal = {
  eats: true,
  walk() {
    /* this method won't be used by rabbit */
  },
};

let rabbit = {
  __proto__: animal,
};

rabbit.walk = function () {
  alert("Rabbit! Bounce-bounce!");
};

rabbit.walk(); // Rabbit! Bounce-bounce!
```

From now on, rabbit.walk() call finds the method immediately in the object and executes it, without using the prototype:

Accessor properties are an exception, as assignment is handled by a setter function. So writing to such a property is actually the same as calling a function.

For that reason admin.fullName works correctly in the code below:

```js
let user = {
  name: "John",
  surname: "Smith",

  set fullName(value) {
    [this.name, this.surname] = value.split(" ");
  },

  get fullName() {
    return `${this.name} ${this.surname}`;
  },
};

let admin = {
  __proto__: user,
  isAdmin: true,
};

alert(admin.fullName); // John Smith (*)

// setter triggers!
admin.fullName = "Alice Cooper"; // (**)
```

Here in the line (\*) the property admin.fullName has a getter in the prototype user, so it is called. And in the line (\*\*) the property has a setter in the prototype, so it is called.

HowTo call a prototype method that is hidden by an object method:

- `Person.prototype.getName.call(this);`
- Ref: https://stackoverflow.com/questions/11542192/override-function-in-javascript

### [Advanced] for..in loop

https://javascript.info/prototype-inheritance#for-in-loop

The for..in loop iterates over inherited properties too.
If that’s not what we want, and we’d like to exclude inherited properties, there’s a built-in method obj.hasOwnProperty(key): it returns true if obj has its own (not inherited) property named key.

### [DEPRECATED] **proto**

Ref:

- https://javascript.info/prototype-methods
- https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes

`__proto__` is a historical getter/setter for [[Prototype]]

Please note that `__proto__` is not the same as [[Prototype]]. It’s a getter/setter for it.

It exists for historical reasons. In modern language it is replaced with functions `Object.getPrototypeOf/Object.setPrototypeOf` that also get/set the prototype. We’ll study the reasons for that and these functions later.

By the specification, **proto** must only be supported by browsers, but in fact all environments including server-side support it. For now, as **proto** notation is a little bit more intuitively obvious, we’ll use it in the examples.

## "(Prototypal) Inheritance"

We traditionally think of "inheritance" as being a relationship between two "classes", rather than between "class" and "instance". Until now we saw only this kind of relationship.

In JS you can achive inheritance creating setting up Prototype Chain (prototype linkage). It's important to notice that it's still a linkage between objects, that create a delegation mechanism.

here's the typical "prototype style" code that creates such links:

```js
function Foo(name) {
  this.name = name;
}

Foo.prototype.myName = function () {
  return this.name;
};

function Bar(name, label) {
  Foo.call(this, name);
  this.label = label;
}

// here, we make a new `Bar.prototype`
// linked to `Foo.prototype`
Bar.prototype = Object.create(Foo.prototype);

// Beware! Now `Bar.prototype.constructor` is gone,
// and might need to be manually "fixed" if you're
// in the habit of relying on such properties!

Bar.prototype.myLabel = function () {
  return this.label;
};

var a = new Bar("a", "obj a");

a.myName(); // "a"
a.myLabel(); // "obj a"
```

The important part is `Bar.prototype = Object.create( Foo.prototype )`. `Object.create(..)` creates a "new" object out of thin air, and links that new object's internal [[Prototype]] to the object you specify (Foo.prototype in this case).

In other words, that line says: "make a new 'Bar dot prototype' object that's linked to 'Foo dot prototype'."

When function `Bar() { .. }` is declared, Bar, like any other function, has a .prototype link to its default object. But that object is not linked to Foo.prototype like we want. So, we create a new object that is linked as we want, effectively throwing away the original incorrectly-linked object.

Note: A common mis-conception/confusion here is that either of the following approaches would also work, but they do not work as you'd expect:

```js
// doesn't work like you want!
Bar.prototype = Foo.prototype;

// works kinda like you want, but with
// side-effects you probably don't want :(
Bar.prototype = new Foo();
```

`Bar.prototype = Foo.prototype` doesn't create a new object for `Bar.prototype` to be linked to. It just makes `Bar.prototype` be another reference to `Foo.prototype`, which effectively links Bar directly to the same object as Foo links to: `Foo.prototype`. This means when you start assigning, like Bar.prototype.myLabel = ..., you're modifying not a separate object but the shared Foo.prototype object itself, which would affect any objects linked to Foo.prototype. This is almost certainly not what you want. If it is what you want, then you likely don't need Bar at all, and should just use only Foo and make your code simpler.

`Bar.prototype = new Foo()` does in fact create a new object which is duly linked to `Foo.prototype` as we'd want. But, it uses the Foo(..) "constructor call" to do it. If that function has any **side-effects** (such as logging, changing state, registering against other objects, adding data properties to this, etc.), those side-effects happen at the time of this linking (and likely against the wrong object!), rather than only when the eventual Bar() "descendants" are created, as would likely be expected.

So, we're left with using Object.create(..) to make a new object that's properly linked, but without having the side-effects of calling Foo(..). The slight downside is that we have to create a new object, throwing the old one away, instead of modifying the existing default object we're provided.

ES6: It would be nice if there was a standard and reliable way to modify the linkage of an existing object. Prior to ES6, there's a non-standard and not fully-cross-browser way, via the .**proto** property, which is settable. ES6 adds a `Object.setPrototypeOf(..)` helper utility, which does the trick in a standard and predictable way.

Compare the pre-ES6 and ES6-standardized techniques for linking Bar.prototype to Foo.prototype, side-by-side:

```js
// pre-ES6
// throws away default existing `Bar.prototype`
Bar.prototype = Object.create(Foo.prototype);

// ES6+
// modifies existing `Bar.prototype`
Object.setPrototypeOf(Bar.prototype, Foo.prototype);
```

Ignoring the slight performance disadvantage (throwing away an object that's later garbage collected) of the Object.create(..) approach, it's a little bit shorter and may be perhaps a little easier to read than the ES6+ approach. But it's probably a syntactic wash either way.

## Classes

REF: [SOJSN2ND] 7.4.1 Using the class keyword

ES6 introduces a new class keyword that provides a much more elegant way of creating objects and implementing inheritance than manually implementing it ourselves with prototypes.

```js
//Defines a constructor function that will be called when we call the class with the keyword new
class Ninja {
  constructor(name) {
    this.name = name;
  }
  //Defines an additional method accessible to all Ninja instances
  swingSword() {
    return true;
  }
}
```

- CONSTRUCTOR: We can explicitly define a constructor function: it will be invoked when instantiating a Ninja, the newly created instance with the this keyword, and we can easily add new properties, such as the name property.
- METHODS: we can also define methods that will be accessible to all Ninja instances (`swingSword()`)
- we can create a Ninja instance by calling the Ninja class with the keyword `new`: `var ninja = new Ninja("Yoshi");`

### CLASSES ARE SYNTACTIC SUGAR

Under the hood we’re still dealing with good old prototypes; classes are syntactic sugar designed to make our lives a bit easier when mimicking classes in JavaScript.

The class above can be translated to functionally identical ES5 code:

```js
function Ninja(name) {
  this.name = name;
}

Ninja.prototype.swingSword = function () {
  return true;
};
```

### Static Methods

```js
class Ninja {
  constructor(name, level) {
    this.name = name;
    this.level = level;
  }

  swingSword() {
    return true;
  }

  //Uses the static keyword to make a static method
  static compare(ninja1, ninja2) {
    return ninja1.level - ninja2.level;
  }
}
```

The compare method, which compares the skill levels of two ninjas, is defined on the class level, and not the instance level! Later we test that this effectively means that the compare method isn’t accessible from ninja instances but is accessible from the Ninja class.

We can also look at how “static” methods can be implemented in pre-ES6 code:

```js
function Ninja(){}
Ninja.compare = function(ninja1, ninja2){...}
```

### Implementing inheritance

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  dance() {
    return true;
  }
}

class Ninja extends Person {
  constructor(name, weapon) {
    super(name);
    this.weapon = weapon;
  }

  wieldWeapon() {
    return true;
  }
}
var person = new Person("Bob");

assert(person instanceof Person, "A person's a person");
assert(person.dance(), "A person can dance.");
assert(person.name === "Bob", "We can call it by name.");
assert(!(person instanceof Ninja), "But it's not a Ninja");
assert(!("wieldWeapon" in person), "And it cannot wield a weapon");
var ninja = new Ninja("Yoshi", "Wakizashi");
assert(ninja instanceof Ninja, "A ninja's a ninja");
assert(ninja.wieldWeapon(), "That can wield a weapon");
assert(ninja instanceof Person, "But it's also a person");
assert(ninja.name === "Yoshi", "That has a name");
assert(ninja.dance(), "And enjoys dancing");
```

## Mixin

TODO

https://github.com/getify/You-Dont-Know-JS/blob/9959fc904d584bbf0b02cf41c192f74ff4238581/objects-classes/ch4.md

See also the second example here: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create#Examples




# Modules, loaders and bundlers.

Ref:

- https://nolanlawson.com/2015/10/19/the-struggles-of-publishing-a-javascript-library/
- Long overview Oct 28, 2018: https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364
- Eloquent_JavaScript.pdf ch 10

## Intro: Modules, Module Loaders, Modules Bundlers

Ref:

- https://www.jvandemo.com/a-10-minute-primer-to-javascript-modules-module-formats-module-loaders-and-module-bundlers/
- https://medium.com/@ajmeyghani/javascript-bundlers-a-comparison-e63f01f2a364
- http://exploringjs.com/es6/ch_modules.html

Why do we need modules?

- to create reusable code
- to provide a clear public **interface** to it
- to state the dependency between reusable code (which other modules need to be present to be able to use a given module and to automatically load dependencies).

We will look at:

- Module formats: what are they and what are the different module definitions for JavaScript.
- Module loaders: what are loaders and how can they be used.
- Module bundlers: what are JavaScript bundlers, what is the process for setting up each, and how do they compare against each other.

The modules ecosystem is quite complex. JavaScript has had modules for a long time. However, they were implemented via libraries, not built into the language. ES6/ES2015 is the first time that JavaScript has built-in modules. EcmaScript 5 and earlier editions were not designed with modules in mind. Over time, developers came up with different patterns to simulate modular design in JavaScript.

### Module Formats Intro

A module format is the syntax we can use to define a module. Before EcmaScript 6 or ES2015, JavaScript did not have an official syntax to define modules. Therefore, smart developers came up with various formats to define modules in JavaScript. Some of the most widely adapted and well known formats are:

- Asynchronous Module Definition (AMD)
- CommonJS
- Universal Module Definition (UMD)
- System.register
- ES6 module format

- Module bundlers: what are JavaScript bundlers, what is the process for setting up each, and how do they compare against each other.

### Module Loaders Intro

Module loaders are used to load JavaScript modules at runtime, usually for development. Most notable loaders are:

- RequireJS: a library
- SystemJS:

becaouse the JS standard different module definitions for JavaScript

### Module Bundlers Intro

Module bundlers are used to bundle several modules into one or more optimized bundles for the browser. Most notable bundlers are:

- Webpack,
- SnowPack (nice one!)
- Rollup,
- Google Closure Compiler.
- Parcel
- Broserify

The Google Closure Compiler (Closure) is a code analyzer and optimizer that can also be used to create bundles. Closure is probably the most mature analyzer and optimizer out there. If you want to analyze your code and output the most optimized code possible, Closure will be your best friend. Rollup has a great Closure plugin that I’m going to cover later.

Most of the bundlers these days have very similar features.

**Tree Shaking**
The one feature that varies among them is tree shaking for CJS or ES modules (dead-code elimination). Out of all the bundlers, Webpack has the most consistent built-in support for ES and CJS module tree shaking. Rollup and Parcel do have tree shaking but Webpack’s is just a little better overall. Parcel however is working on making tree shaking available for both CJS and ES modules. Until tree shaking matures among bundlers it’s best to carefully examine what you are importing to minimize the final bundle size.
Overall all bundlers are pretty fast if you are careful about what you are importing. In the worst case in can take up to 7 seconds to bundle a very simple project.

Zero-config or not, you’ll have to spend some time experimenting with each bundler to learn them well. If a bundler is labelled as zero-config that does not mean that you don’t have to configure anything for production. It’s mostly true for development, but for production you have to create configuration files regardless. I think a better term would have been “bundlers for development”, rather than “bundlers with zero configuration”.

Tree Shaking:

- ref: https://webpack.js.org/guides/tree-shaking/
- Tree shaking is a term commonly used in the JavaScript context for **dead-code elimination**. It relies on the static structure of ES2015 module syntax, i.e. import and export. The name and concept have been popularized by the ES2015 module bundler rollup.

## History: Pre 2015

[JSFIP](https://exploringjs.com/impatient-js/ch_modules.html#scripts): another point of view about using js script manually.

Riassunto:

- ESM looks like the best modularity pattern
  - Browser support is good
  - NodeJS has experimental support (https://nodejs.org/api/esm.html#esm_package_exports)
  - TypeScript use this format
- CJS is still the way to go in NodeJS JS app. Many lib for NodeJS

TL;DR: In 2020 learn ESM first and then CJS if you need to use NodeJS

Until 2015, the JavaScript language had no built-in module system.

When JavaScript was first introduced it had a very basic system for loading “modules”. It involved including a script tag in an html file and the location of the JavaScript file. This mechanism wasn’t good, even for small projects because:

Everything was loaded in the global context leading to name collisions and overrides
It involved a lot of manual work by the developer to figure out the dependencies and the order of inclusion
These types of problems were exasperated as the client-side (browser) applications grew bigger and bigger and more complex. In order to solve the module problem two module definitions were introduced by the community around 2009. These module definitions were the CommonJS (CJS) and the Asynchronous Module Definition (AMD).

You can use JavaScript functions to create local scopes and objects to represent module interfaces.

```
const weekDay = function() {
const names = ["Sunday", "Monday", "Tuesday", "Wednesday",
"Thursday", "Friday", "Saturday"];
   return {
     name(number) { return names[number]; },
     number(name) { return names.indexOf(name); }
}; }();
console.log(weekDay.name(weekDay.number("Sunday"))); // → Sunday
```

Its interface consists of weekDay.name and weekDay .number, and it hides its local binding names inside the scope of a function expression that is immediately invoked.

This style of modules provides isolation, to a certain degree, but it does not declare dependencies. Instead, it just puts its interface into the global scope and expects its dependencies, if any, to do the same.

Just putting your JavaScript code into different files does not satisfy these requirements. The files still share the same global namespace.

**For a long time this was the main approach used in web programming, but it is mostly obsolete now.**

## NON Standard formats: CommonJS, AMD-RequireJS, UMD

Let's have a quick look at each one of them so you can recognize their syntax.

Two prominent module definitions were developed as part of the community effort: `CJS (CommonJS)` and `AMD (Asynchronous Module Definition)`.

`CommonJS` format:

- Main Target: Backend.
- was defined as a **synchronous** definition intended for **server-side JavaScript**.
- Node’s module system is practically based on CJS with some minor differences.
- uses `require` and `module.exports` to define dependencies and modules
- CommonJS modules work quite well and, in combination with NPM, have allowed the JavaScript community to start sharing code on a large scale. But now is obsolete.
- The imported result is a copy of the imported object.

```
var dep1 = require('./dep1');
var dep2 = require('./dep2');

module.exports = function(){
  // ...
}
```

`AMD` format:

- Main Target: Frontend
- Imports modules: Asynchronously.
- was defined an **asynchronous** model intended for modules in the browser
- `RequireJS` is the most popular implementation of AMD.
- The AMD format is used in browsers and uses a `define` function to define modules

```
//Calling define with a dependency array and a factory function
define(['dep1', 'dep2'], function (dep1, dep2) {

    //Define the module value by returning a value.
    return function () {};
});
```

`UMD` format:

- Main Target: Frontend and Backend (“Universal”).
- UMD stands for Universal Module Definition. It’s essentially a piece of JavaScript code placed at the top of libraries that enables any loader to load them regardless of the environment they are in.
- It's more like an interface for bringing compatibility in Frontend and Backend environments to both AMD and CJS.

`ESM - ECMAScript Modules (2015)` format:

- Main Target: Frontend and Backend.
- A standard module system was finally introduced in 2015 as part of the ES2015 (ES6) specification. It defined the semantics for importing and exporting modules asynchronously.
- Works in many modern browsers
- Tree-shaking support due to ES6's static module structure

Ref:

- Eloquent_JavaScript.pdf ch 10

## Current state of Modules in Node.js

2020 July:

- With the release of Node version 13.9.0, ES modules can now be used without an experimental flag since they are enabled by default.

- https://2ality.com/2019/10/hybrid-npm-packages.html
- https://blog.logrocket.com/es-modules-in-node-today/
- https://medium.com/@nirsky/make-your-npm-package-work-on-both-node-js-and-browser-58bff1a18f55

2019 July :
https://blog.logrocket.com/es-modules-in-node-js-12-from-experimental-to-release/

## ESM ES6/ES2015 Modules: Standard Javascript Modules

- [javascript.info Modules](https://javascript.info/modules-intro)
  - Good intro for beginners
  - Super brief History of modules
  - basic usage of import/export with browser example
  - `<script type="module">` : Always "use strict", Module-level scope, A module code is evaluated only the first time when imported, import.meta, "this" is undefined, Module scripts are deferred, `<script async type="module">` , External scripts, No “bare” modules allowed, Compatibility, “nomodule”,

- https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules


- [CommonJS vs. ES Modules: Modules and Imports in NodeJS in 2022](https://reflectoring.io/nodejs-modules-imports/)



- [JSFIP Modules ES2020](https://exploringjs.com/impatient-js/ch_modules.html)
- [Yeuda draft](https://gist.github.com/wycats/51c96e3adcdb3a68cbc3)
- http://eviltrout.com/2014/05/03/getting-started-with-es6.html


As our application grows bigger, we want to split it into multiple files, so called “modules”. A module may contain a class or a library of functions for a specific purpose.

For a long time, JavaScript existed without a language-level module syntax. That wasn’t a problem, because initially scripts were small and simple, so there was no need. 

But eventually scripts became more and more complex, so the community invented a variety of ways to organize code into modules, special libraries to load modules on demand. UMD, AMD, was 

JavaScript standard from 2015 introduces its own, different module system. It is usually called ES modules (ESM), where ES stands for ECMAScript.

In 2022 modern browsers, NodeJS 14 and typescript support ESM. So if you are starting a new project, use ES Modules ( ref https://reflectoring.io/nodejs-modules-imports/ ).

The full standard of ES modules comprises the following parts:

1. Syntax (how code is written): What is a module? How are imports and exports declared? Etc.
2. Semantics (how code is executed): How are variable bindings exported? How are imports connected with exports? Etc.
3. A programmatic loader API for configuring module loading (https://javascript.info/modules-dynamic-imports). Usecase: conditional imports.


A **module** is simply a file with JavaScript code in it. By default anything you declare in a file in a ES6 project is not available outside that file. You have to use the export keyword to explicitly make it available, defining the **module interface**. An ES module’s interface is not a single value but a set of named bindings. Modules can load each other and use special directives `export` and `import` to interchange functionality, call functions of one module from another one.

`export` keyword labels variables and functions that should be accessible from outside the current module.

The easiest way to use it is to place it in front of any items you want exported out of the module, for example to export the `name` variable and the `draw` function:

```js
export const name = 'square';

export function draw(ctx, length, x, y, color) {
  ctx.fillStyle = color;
  ctx.fillRect(x, y, length, length);

  return { length, x, y, color };
}
```

`import` allows the import of functionality from other modules:

```js
import { name, draw, reportArea, reportPerimeter } from './modules/square.js';

draw(...) // here we are using a function defined in the square.js file
```


You can export functions, var, let, const, and — as we'll see later — classes. They need to be top-level items; you can't use export inside a function, for example.

A more convenient way of exporting all the items you want to export is to use a single export statement at the end of your module file, followed by a comma-separated list of the features you want to export wrapped in curly braces. For example:

```js
export { name, draw, reportArea, reportPerimeter };
```

WARNING:

- in this paragraph we'll describe the ESM syntax and convention. Many bundlers (ex: Webpack) use a similar syntax but with a slightly different behaviour.


### Default exports versus named exports

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#default_exports_versus_named_exports 

default export — this is designed to make it easy to have a default function provided by a module, and also helps JavaScript modules to interoperate with existing CommonJS and AMD module systems (as explained nicely in [ES6 In Depth: Modules by Jason Orendorff](https://hacks.mozilla.org/2015/08/es6-in-depth-modules/); search for "Default exports").

For example it's very handy to create ReactJS components.
`export default` is used to export a single class, function or primitive from a script file.

The export can also be written as

```js
export default class HelloWorld extends React.Component {
  render() {
    return <p>Hello, world!</p>;
  }
}
```

You could also write this as a function component like

```js
export default function HelloWorld() {
  return <p>Hello, world!</p>
}
```

This is used to import this function in another script file

```js
import HelloWorld from './HelloWorld';
```

You don't necessarily import it as HelloWorld you can give it any name as it's a default export.

Again, note the lack of curly braces. This is because there is only one default export allowed per module, and we know that randomSquare is it. The above line is basically shorthand for:

```js
import {default as randomSquare} from './modules/square.js';
```

### Named Import - Avoiding naming conflicts

If we tried to import different functions of the same name into the same top-level module file, we'd end up with conflicts and errors.

Fortunately there are a number of ways to get around this.

Renaming imports and exports : Inside your import and export statement's curly braces, you can use the keyword as along with a new feature name, to change the identifying name you will use for a feature inside the top-level module.

```js
// inside module.js
export { function1, function2 };

// inside main.js
import {
  function1 as newFunctionName,
  function2 as anotherNewFunctionName,
} from './modules/module.js';
```

See here for more details: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#avoiding_naming_conflicts


### Cheatsheet: syntax of ECMAScript modules

Ref: [JSFIP Modules ES2020](https://exploringjs.com/impatient-js/ch_modules.html#overview-syntax-of-ecmascript-modules)

#### 24.1.1 Exporting

```js
// Named exports
export function f() {}
export const one = 1;
export { foo, b as bar };

// Default exports
export default function f() {} // declaration with optional name
// Replacement for `const` (there must be exactly one value)
export default 123;

// Re-exporting from another module
export * from "./some-module.mjs";
export { foo, b as bar } from "./some-module.mjs";
```

#### 24.1.2 Importing

```js
// Named imports
import { foo, bar as b } from "./some-module.mjs";
// Namespace import
import * as someModule from "./some-module.mjs";
// Default import
import someModule from "./some-module.mjs";

// Combinations:
import someModule, * as someModule from "./some-module.mjs";
import someModule, { foo, bar as b } from "./some-module.mjs";

// Empty import (for modules with side effects)
import "./some-module.mjs";
```

### Named Export

Each module can have zero or more named exports.

We can label any declaration as exported by placing export before it, be it a variable, function or a class.

For instance, here all exports are valid:

```js
// export an array
export let months = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

// export a constant
export const MODULES_BECAME_STANDARD_YEAR = 2015;

// export a class
export class User {
  constructor(name) {
    this.name = name;
  }
}
```

Also, we can put export separately from declarations.

Here we first declare, and then export:

```js
// 📁 say.js
function sayHi(user) {
  alert(`Hello, ${user}!`);
}

function sayBye(user) {
  alert(`Bye, ${user}!`);
}

export { sayHi, sayBye }; // a list of exported variables
```

...Or, technically we could put export above functions as well.

Summary:

- To export something, we put the keyword export in front of a declaration.
- Entities that are not exported are private to a module and can’t be accessed from outside.

WARNING: No semicolons after export class/function

Please note that export before a class or a function does not make it a function expression. It’s still a function declaration, albeit exported.

Most JavaScript style guides don’t recommend semicolons after function and class declarations.

That’s why there’s no need for a semicolon at the end of export class and export function:

```js
export function sayHi(user) {
  alert(`Hello, ${user}!`);
} // no ; at the end
```

### Named Export

### example

File structure:

```bash
calculator/
  lib/
    calc.js
  main.js
```

Define a module:

```javascript
//------ lib.js ------
export const sqrt = Math.sqrt;
export function square(x) {
  return x * x;
}
export function diag(x, y) {
  return sqrt(square(x) + square(y));
}
```

Use a module:

```javascript
//------ main.js ------
import { square, diag } from "lib";
console.log(square(11)); // 121
console.log(diag(4, 3)); // 5
```

you can also import the whole module and refer to its named exports via property notation:

```javascript
//------ main.js ------
import * as lib from "lib";
console.log(lib.square(11)); // 121
console.log(lib.diag(4, 3)); // 5
```

### Traspiler

The great news is you can use ES6 modules today! You just have to run your code through a **transpiler**

[ES6 module transpiler](https://github.com/esnext/es6-module-transpiler)
is a JavaScript library for converting JavaScript files written using the ES6 draft specification module syntax to existing library-based module systems such as AMD, CommonJS, or simply globals.
This [post](http://esnext.github.io/es6-module-transpiler/) introduce how the traspiler works.

The subset of the ES6 module syntax supported by the transpiler is described [here](https://github.com/esnext/es6-module-transpiler#supported-es6-module-syntax)

#### ES6 Module transpiler

- [ES6 Module Traspiler](https://github.com/esnext/es6-module-transpiler)
- [NPM node package](https://www.npmjs.com/package/es6-module-transpiler): npm install -g es6-module-transpiler

- [Broccoli Plugin](https://github.com/mmun/broccoli-es6-module-transpiler)

Supported syntax : https://github.com/esnext/es6-module-transpiler#supported-es6-module-syntax

How use it?

- rsvp

### HOW-TO ESM and Browser

The import statement cannot be used in embedded scripts unless such script has a type="module":

```html
<script type="module">
  ....
</script>

------------------------------------------

<!DOCTYPE html>
<script type="module">
  import { sayHi } from "./say.js";
  document.body.innerHTML = sayHi("John");
</script>
```

```js
//say.js
export function sayHi(user) {
  return `Hello, ${user}!`;
}
```

WARNING! : Modules work only via HTTP(s), not in local files

If you try to open a web-page locally, via `file://` protocol, you’ll find that import/export directives don’t work. Use a local web-server, such as static-server or use the “live server” capability of your editor, such as VS Code Live Server Extension to test modules.

Ref: [JSINFO](https://javascript.info/modules-intro)

- Good intro to ESM for beginners
- Super brief History of modules
- basic usage of import/export with browser example
- `<script type="module">` : Always "use strict", Module-level scope, A module code is evaluated only the first time when imported

#### [ADVANCED] import.meta

#### [ADVANCED] In a module, top-level "this" is undefined.

So the global scope pollution is avoided by desing. Ref: https://javascript.info/modules-intro#in-a-module-this-is-undefined

Compare it to non-module scripts, where this is a global object:

```js
<script>
  alert(this); // [object Window]
</script>

<script type="module">
  alert(this); // undefined
</script>
```

#### [ADVANCED] Module scripts are deferred

In other words:

- downloading external module scripts `<script type="module" src="...">`doesn’t block HTML processing, they load in parallel with other resources.
- module scripts wait until the HTML document is fully ready (even if they are tiny and load faster than HTML), and then run.
- relative order of scripts is maintained: scripts that go first in the document, execute first.

As a side-effect, module scripts always “see” the fully loaded HTML-page, including HTML elements below them.

```js
<script type="module">
  alert(typeof button); // object: the script can 'see' the button below
  // as modules are deferred, the script runs after the whole page is loaded
</script>

Compare to regular script below:

<script>
  alert(typeof button); // Error: button is undefined, the script can't see elements below
  // regular scripts run immediately, before the rest of the page is processed
</script>

<button id="button">Button</button>
```

Please note: the second script actually runs before the first! So we’ll see undefined first, and then object.

That’s because modules are deferred, so we wait for the document to be processed. The regular script runs immediately, so we see its output first.

When using modules, we should be aware that the HTML page shows up as it loads, and JavaScript modules run after that, so the user may see the page before the JavaScript application is ready. Some functionality may not work yet. We should put “loading indicators”, or otherwise ensure that the visitor won’t be confused by that.

#### [ADVANCED] Async on inline scripts

If you add the `async` keyword:

```js
<script async type="module">
```

The module async scripts run immediately when ready, independently of other scripts or the HTML document (otherwise it would have waited the previous html and script tags).

Also non module script support async but only works on external scripts, For module scripts, it works on inline scripts as well.

USE-CASES: functionality that doesn’t depend on anything, like counters, ads, document-level event listeners.

```js
<!-- all dependencies are fetched (analytics.js), and the script runs -->
<!-- doesn't wait for the document or other <script> tags -->
<script async type="module">
  import {counter} from './analytics.js';

  counter.count();
</script>
```

#### [ADVANCED] External module scripts

External scripts that have type="module" are different in two aspects:

1. External scripts with the same src run only once:

```js
<!-- the script my.js is fetched and executed only once -->
<script type="module" src="my.js"></script>  <!-- FETCH AND LOAD!!! -->
<script type="module" src="my.js"></script>  <!-- DO NOTING!!! -->
```

2. External scripts that are fetched from another origin (e.g. another site) require CORS headers, as described in the chapter Fetch: Cross-Origin Requests. In other words, if a module script is fetched from another origin, the remote server must supply a header Access-Control-Allow-Origin allowing the fetch.

```js
<!-- another-site.com must supply Access-Control-Allow-Origin -->
<!-- otherwise, the script won't execute -->
<script type="module" src="http://another-site.com/their.js"></script>
That ensures better security by default.
```

#### [ADVANCED] No “bare” modules allowed in a Browser

In the browser, import must get either a relative or absolute URL. Modules without any path are called “bare” modules. Such modules are not allowed in import.

For instance, this import is invalid:

```js
import { sayHi } from "sayHi"; // Error, "bare" module
// the module must have a path, e.g. './sayHi.js' or wherever the module is
```

Certain environments, like Node.js or bundle tools allow bare modules, without any path, as they have their own ways for finding modules and hooks to fine-tune them. But browsers do not support bare modules yet.

#### [ADVANCED] Compatibility, “nomodule”

Old browsers do not understand type="module". Scripts of an unknown type are just ignored. For them, it’s possible to provide a fallback using the nomodule attribute:

```js
<script type="module">
  alert("Runs in modern browsers");
</script>

<script nomodule>
  alert("Modern browsers know both type=module and nomodule, so skip this")
  alert("Old browsers ignore script with unknown type=module, but execute this.");
</script>
```

#### A notes about build tools

SEE https://javascript.info/modules-intro#build-tools

TL;DR: In real-life, browser modules are rarely used in their “raw” form. Usually, we bundle them together with a special tool such as Webpack and deploy to the production server (Eventhough it's really useful to use them raw when you teach or do some quick esperiment). That's why we use babel, webpack etc

### HOW-TO ESM and NodeJS

Native support for ES modules in Node.js:

- Node.js 12+ supports ESM natively behind the flag --experimental-modules
- Node.js 13.2.0+ supports native ESM without that flag.

Ref:

- https://nodejs.org/api/esm.html#esm_ecmascript_modules

Node.js will treat the following as ES modules when passed to node as the initial input, or when referenced by import statements within ES module code:

- Files ending in `.mjs`.

- Files ending in .js when the nearest parent package.json file contains a top-level field `"type"` with a value of `"module"`.

- Strings passed in as an argument to --eval, or piped to node via STDIN, with the flag --input-type=module.

Node.js will treat as CommonJS all other forms of input, such as .js files where the nearest parent package.json file contains no top-level "type" field, or string input without the flag --input-type. This behavior is to preserve backward compatibility. However, now that Node.js supports both CommonJS and ES modules, it is best to be explicit whenever possible. Node.js will treat the following as CommonJS when passed to node as the initial input, or when referenced by import statements within ES module code:

- Files ending in .cjs.

- Files ending in .js when the nearest parent package.json file contains a top-level field "type" with a value of "commonjs".

- Strings passed in as an argument to --eval or --print, or piped to node via STDIN, with the flag --input-type=commonjs

### HOW-TO write Hybrid npm packages (ESM and CommonJS)

https://2ality.com/2019/10/hybrid-npm-packages.html

### ES6Modules

- https://github.com/ember-cli/broccoli-es6modules

ES6Modules wraps the esperanto library. All options described for esperanto can be provided here.

### Esperanto

Refs:

- [Homepage](http://esperantojs.org/)
- [Github Homepage](https://github.com/esperantojs/esperanto)

Esperanto is a tool for converting ES6 modules to AMD, CommonJS or UMD. It's built for speed, interoperability and ease of use.

How use it?

- Ember.js

## Node Modules

Ref:

- [Intro doc](https://github.com/maxogden/art-of-node/#modular-development-workflow)
- [Official doc](https://nodejs.org/api/modules.html)
- [Module Intenals] https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6

TODO:

- Does NodeJS support es6 modules in 2019? https://medium.com/the-node-js-collection/an-update-on-es6-modules-in-node-js-42c958b890c
- `export`
- `require`
- `require.resolve`

In Node, the modularity is a first-class concept. In the Node.js module system, each file is treated as a separate module.

So, if you are creating, let’s say, a demo.js file, this implies you are creating a module in Node. Basically modules help us encapsulating our code into manageable chunks.
Anything that we define in our module (i.e. in our JavaScript file) remains limited to that module only, unless we want to expose it to other parts of our code.

So, anything we define inside our module remains private to that module only.

The NodeJS module system is derived from CommonJS.

One of the useful tools Node.js adds on top of standard ECMAScript is a notation for defining and using modules.

`require()` is a function for loading code from other files, it returns the exports of the module name that you specify.

```
var uniq = require('uniq');
var nums = [ 5, 2, 1, 3, 2, 5, 4, 2, 0, 1 ];
console.log(uniq(nums));
```

Note that `require()` returned a function and we assigned that return value to a variable called uniq. We could have picked any other name and it would have worked the same. `require()` returns the exports of the module name that you specify.

TODO:

- `export`
- `require`
- `require.resolve`

A "module" exports objects and functions by adding them to exports, and another module can import it by using require. The semantics are explained well in the official documentation.

`module.exports` is the object that's actually returned as the result of a `require` call.

To test out which module actually gets loaded by node, you can use the `require.resolve('some_module')` command

In the next paragraphs we will see how modularity was implement before NodeJS and then how NodeJS implemented modularity.

### How Modularity Worked Before ES5 and NodeJS

Ref: https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6

Prior to modules in Node.js or ES5 modules, the modularity in JavaScript was achieved using IIFE (Immediately Invoked Function Expression), which is, as the name suggests, a function which is invoked immediately after it is defined.

```
(function () {
  const sum = (a, b) => {
    return a + b;
  };
  const result = sum(2, 3)
  console.log(result)
})()

sum(5, 8) // ReferenceError: sum not defined
```

Now, if we run this code, we will get the output as 5.
The function sum is defined inside this IIFE and if any code outside that IIFE tries to access the sum function, it will result in ReferenceError: sum is not defined, i.e. the sum function is private to this particular IIFE.
So, how do we access this sum function outside of this IIFE?

```
const exportObj = {};
(function () {
  const sum = (a, b) => {
    return a + b;
  };
  const result1 = sum(2, 3)
  console.log(result1) //5
  exportObj.sum = sum;
})()
const result2 = exportObj.sum(5, 8)
console.log(result2) // 13
```

To expose our sum function outside IIFE, we create an object (exportObj) outside IIFE, then, through closure, we access that object inside our IIFE and assign our sum function to one of its property.
After that, we call the sum function on the exportObj object outside the IIFE. This time, we are able to get result without any errors.

### How Modularity Works in Node.js

We have seen above that, to achieve modularity prior to Node and ES5, we used functions.
In Node.js, this wrapping function that wraps our code is not written by us but is automatically added by Node for us.

Let’s look at an example to understand it better. Let’s say we defined one file, named sum.js, with the following content:

```
const sum = (a, b) => {
  return a + b;
};

const result = sum(2, 3)
console.log(result)
```

https://gist.github.com/udittyagi/e4b49683361c49fbff2fb3c5e62f93e7#file-sum-js

So, in Node.js, this code is wrapped and looks something like this in our running environment:

```
(function (exports, require, module, __filename, __dirname) {
  // Module code actually lives in here
  const sum = (a, b) => {
    return a + b;
  };

  const result = sum(2, 3)
  console.log(result)
});
```

https://gist.github.com/udittyagi/aa3c99a05504a210fa44249ac1477dad#file-summodule-js

Everything is wrapped as we wrapped in our IIFE but, here, this wrapper function gets some arguments. We will discuss them in detail later.

To check whether your code is wrapped in a function and whether we are receiving these arguments, or not. In JavaScript, we know that all functions receive an argument called arguments, so, if we get arguments in our code, it confirms that our code is inside a function: `console.log('Arguments given by node', arguments)`

Example HERE: https://github.com/breezeight/javascript_nicola_courses/blob/master/node-modules-under-the-hood/README.md

We can see that we get the output of arguments (arguments is an array-like object, whose keys are numeric, which is passed to every function by default). So, it confirms that our code is wrapped inside a function and that function receives five arguments, which are given by Node.js.
Let’s discuss these five arguments one-by-one.

#### Exports

This is an object used to expose our functionalities in one module, so these functionalities can be used in other modules.

We can expose anything, this can be a function, variable, constants, classes, etc. As we have done above in the How modularity worked before section, we have created a property on exportObj and then assigned a value to it.

The same way we do it with exports object — we create a property on the exports object and then assign a value, or whatever you want to expose (variable, function, classes, constants), to that property.

```
const sum = (a, b) => {
  return a + b;
};
const multiply = (a, b) => {
  return a * b
};
exports.multiply = multiply;
```

Here, we expose the multiply function by assigning the function reference to a newly created multiply property on the exports object, i.e. multiply function is only available outside this module, not the sum function.
Note: Do not provide a new reference to this exports object, i.e. don’t assign a new object to the exports argument. (We will discuss why not to do this.)

#### Require

This is a function that we use to import or require the functionalities from other modules. It is a compliment to the exports object, which is used to export functionalities. require, on the other hand, is used to import those functionalities.

To require a module, we call the require function with either the path of the module (absolute or relative), which starts with /, ./, or ../ in the case of local modules, or the name of the module in the case of core modules and third-party modules.
Then, it returns the exported content of the module that we require.

Note: Basically, we get the reference of the object module.exports (we will discuss this) when we require a module.

```
const os = require('os'); //node's core module
const express = require('express') // third party module
const operations = require('./operations.js'); //local module

//Do something with these modules
const result1 = operations.multiply(2, 4);
console.log('Multiply Result: ', result1)// 8

const result2 = operations.sum(2, 3);// Error, as it is not exported.
console.log('Sum Result: ', result2)
```

We implemented two functions, sum and multiply, but we have exported only multiply, so only that one is available outside of the operations.js module. That is why we will get an error if we try to call sum.
Node’s require function has a lot more to offer than just importing the functionalities, we will dive deeper into this.

#### Module

This is the third argument passed, the module variable is a reference to the object representing the current module. It has various useful properties which we can see in the terminal with `console.log(module)` in any module.

The module object contains all the data regarding our module, such as:

- “Who is its parent? Who are its children?
- What are all the paths it took to resolve third-party modules?
- Is it completely loaded, or not?”

But the most important property of the module object is the exports property, we can also use this exports property on the module to export our data, rather than using exports arguments of the wrapper function.

```
const sum = (a, b) => {
  return a + b;
};
const multiply = (a, b) => {
  return a * b
};

module.exports = {
  sum,
  multiply
}
```

So, this is the second way of exporting functionalities out of our module.
Note: We will see the difference between exports and module.exports, and how they are connected to each other.

Summary of the module object

- module.filename is the fully resolved filename of the module.
- module.id is the identifier for the module. Typically, this is the fully resolved filename, except for the main module, it is ‘.’ (period), see pic 3. Main module is the module that spins up your Node application, e.g if we write node app.js in the terminal, then app.js is the main module.
- module.path is the directory name of your name module.
- module.parent is an object which refers to the parent module.
- module.children is an array of all the children module objects.
- module.loaded is a boolean property which tells us whether or not the module is done loading, or is in the process of loading.
- module.paths is an array of all the paths that Node will look up to resolve a module.

TODO: rileggere la question di delle [CIRCULAR] reference qua https://medium.com/better-programming/node-js-modules-basics-to-advanced-2464001229b6

Some of you might have noticed in pic 2 and pic 3, this weird [Circular] thing in module parent or children property. So, what is that?
Actually, [Circular] defines a circular reference, as in pic 2, which prints out the module object of operations.js. The parent property of the operations.js module references the app.js module.
Similarly, operations.js is a child module of app.js, so its children property should have a reference to the operations.js module. And, similarly, the operations.js module parent property again refers to the app.js module, so it will go into this infinite loop.
To prevent this infinite loop, Node sees that, if any module’s parent or child is already loaded, it will not load them again and show this [Circular] instead.

#### filename

This is a variable that contains the absolute path of the current module.
Given two modules: a and b, where b is a dependency of a and there is a directory structure of:
/User/home/node_blog/a.js
/User/home/node_blog/node_modules/b/b.js
So, if we do console.log(**filename)within b.js, we will get /User/home/node_blog/node_modules/b/b.js. If we do console.log(**filename) within a.js, we will get /User/home/node_blog/a.js.

#### dirname

The directory name of the current module. This is the same as the path.dirname() of the **filename.
So, for the above modules, a.js and b.js.
If we do console.log(**dirname) within b.js, we will get /User/home/node_blog/node_modules/b/ and in a.js, we will get /User/home/node_blog/.
Now we have studied the basics of the module. From now on, we will dive deep into this topic. Bear with me a bit longer as there are various interesting things we are going to discuss

#### Difference Between module.exports and exports

We use both `module.exports` and `exports` to export our functionalities out of our module.
But, there is a slight difference between them. Rather, I’ll say that they are not different but they are similar. The `exports` object is just shorthand for `module.exports`.
Inside Node, the exports object refers to the module.exports object. Which is somewhat like: `const exports = module.exports;`

VERY IMPORTANT: when we require in a module, `module.exports` object is returned by the require function.

And that is the reason we don’t change the reference of the exports object, because, if we change the exports object, that will no longer refer to the module.exports, resulting in the functionalities not being exported from our module.

Can we use both module.exports and exports in a single module?
Yes, we can, but there are some subtleties we should keep in mind if we are using both.
Those are, when we use require in any module, we get the module.exports object and the exports object referring to module.exports, so it is necessary to maintain this reference.

In the code below, the sum will not be exported as we have changed the reference of module.exports by assigning a new object to it but the exports object now also refers to the previous reference of module.exports.

https://github.com/breezeight/javascript_nicola_courses/blob/master/node-modules-under-the-hood/operations_gotcha.js

Test it:

- git clone git@github.com:breezeight/javascript_nicola_courses.git
- cd javascript_nicola_courses
- node node-modules-under-the-hood/app_export_gotcha.js

#### Modules in Detail

It is not necessary that only a file can be a module that we require. Other than files, we also have folders as modules that we can require in.

Generally, a folder as a module is a module of modules, i.e. it contains various modules inside it to achieve functionality. This is what libraries do, they are organized in a self-contained directory and then they provide a single entry point to that directory.

There are two ways in which we can require a folder.

- Create a package.json in the root of the folder, which specifies a main module. An example package.json file might look like this:

```
{ "name" : "some-library",
  "main" : "./lib/some-library.js" }
```

If this was in a folder at ./some-library, then require('./some-library') would attempt to load ./some-library/lib/some-library.js.

This is the extent of Node.js awareness of package.json.

- If Node does not find any package.json in the root directory of the module, or in package.json if the main entry is missing or cannot be resolved. Then, Node.js will try to load index.js or index.node from that directory. For example, if there was no package.json file in the above example, then require('./some-library') would attempt to load:
- ./some-library/index.js
- ./some-library/index.node

If these attempts fail, then Node.js will report the entire module as missing with the default error: `Error: Cannot find module ‘some-library’.`

In file modules, .js file is also not the only module, we have .json files and .node files, they are also modules in Node.

#### Requiring in Detail

When we require a module it is not necessary to give the file extension. For example, if there is a `some-file.js` file that we want to require and it is on the same level, we can require it as: `const someFile = require(‘./some-file’);`
That is without specifying the extension.
While resolving the path of this file, Node follows a procedure.
It first looks for some-file.js, if some-file.js is not present, it will look for some-file.json and if that is also not present, it will look for some-file.node.
.js files are interpreted as JavaScript text files, and .json files are parsed as JSON text files, i.e. we get the JavaScript object. .node files are interpreted as compiled add-on modules.

### How require looks for files

Ref: https://github.com/browserify/browserify-handbook/blob/master/readme.markdown#how-node_modules-works

**Relative** path : Paths that start with a `./` or `../` are always local to the file that calls require()

- `require('./foo.js');` : load a file foo.js from the same dir of your main.js file
- `require('../foo.js');` : load from the parent dirs\*

**Non-relative** path: such as `require('xyz')` from /beep/boop/foo.js, node searches these paths in order, stopping at the first match and raising an error if nothing is found:

- `/beep/boop/node_modules/xyz`
- `/beep/node_modules/xyz`
- `/node_modules/xyz`

For each xyz directory that exists, node will:

- first look for an `xyz/package.json` to see if a `main` field exists. The "main" field defines which file should take charge if you require() the directory path.
- second, if there is no package.json or no "main" field, index.js is assumed

Example 1: if /beep/node_modules/xyz is the first match and /beep/node_modules/xyz/package.json has:

```
{
  "name": "xyz",
  "version": "1.2.3",
  "main": "lib/abc.js"
}
```

then the exports from /beep/node_modules/xyz/lib/abc.js will be returned by require('xyz').

Example 2: If there is no package.json or no "main" field, `index.js` is assumed: `/beep/node_modules/xyz/index.js`

If you need to, you can reach into a package to pick out a particular file. For example, to load the lib/clone.js file from the dat package, just do:

```
var clone = require('dat/lib/clone.js')
```

The recursive node_modules resolution will find the first dat package up the directory hierarchy, then the `lib/clone.js` file will be resolved from there. This `require('dat/lib/clone.js')` approach will work from any location where you can require('dat').

### What is an export?

A "module" exports objects and functions by adding them to exports, and another module can import it by using require. The semantics are explained well in the official documentation.

`module.exports` is the object that's actually returned as the result of a `require` call.

To test out which module actually gets loaded by node, you can use the `require.resolve('some_module')` command

### Node.js: Require VS import

- `require` is defined by the node module system
- `import` ???? the rsvp npm package use it.... but other package no (ex: https://github.com/strongloop/express) WHY??? WHAT is the DIFFERENCE?

may be reading this will answer: https://appdividend.com/2019/01/23/javascript-import-statement-tutorial-with-example/

https://medium.com/@geekguy/javascript-modues-exports-vs-exports-whats-the-difference-9a61cdb99386

### HOWTO write a module

https://github.com/maxogden/art-of-node/#how-to-write-a-module

- By default node tries to load module/index.js when you require('module'), any other file name won't work unless you set the main field of package.json to point to it.

### Require package

https://www.npmjs.com/package/resolve

### Internals

- http://eli.thegreenplace.net/2013/05/27/how-require-loads-modules-in-node-js
- https://github.com/joyent/node/blob/master/lib/module.js#L380
- What is the purpose of Node.js module.exports and how do you use it? http://stackoverflow.com/questions/5311334/what-is-the-purpose-of-node-js-module-exports-and-how-do-you-use-it
