"""
Python module generated from Java source file com.google.gson.internal.bind.TypeAdapters

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import JsonArray
from com.google.gson import JsonElement
from com.google.gson import JsonIOException
from com.google.gson import JsonNull
from com.google.gson import JsonObject
from com.google.gson import JsonPrimitive
from com.google.gson import JsonSyntaxException
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.annotations import SerializedName
from com.google.gson.internal import LazilyParsedNumber
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.math import BigDecimal
from java.math import BigInteger
from java.net import InetAddress
from java.net import URI
from java.net import URISyntaxException
from java.net import URL
from java.util import BitSet
from java.util import Calendar
from java.util import Currency
from java.util import Date
from java.util import GregorianCalendar
from java.util import Locale
from java.util import StringTokenizer
from java.util import UUID
from java.util.concurrent.atomic import AtomicBoolean
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.atomic import AtomicIntegerArray
from typing import Any, Callable, Iterable, Tuple


class TypeAdapters:
    """
    Type adapters for basic types.
    """

    CLASS = TypeAdapter<Class>() {
    
        @Override
        public void write(JsonWriter out, Class value) throws IOException {
            if (value == null) {
                out.nullValue();
            } else {
                throw UnsupportedOperationException("Attempted to serialize java.lang.Class: " + value.getName() + ". Forgot to register a type adapter?");
            }
        }
    
        @Override
        public Class read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            } else {
                throw UnsupportedOperationException("Attempted to deserialize a java.lang.Class. Forgot to register a type adapter?");
            }
        }
    }
    CLASS_FACTORY = newFactory(Class.class, CLASS)
    BIT_SET = TypeAdapter<BitSet>() {
    
        @Override
        public BitSet read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            BitSet bitset = BitSet();
            in.beginArray();
            int i = 0;
            JsonToken tokenType = in.peek();
            while (tokenType != JsonToken.END_ARRAY) {
                boolean set;
                switch(tokenType) {
                    case NUMBER:
                        set = in.nextInt() != 0;
                        break;
                    case BOOLEAN:
                        set = in.nextBoolean();
                        break;
                    case STRING:
                        String stringValue = in.nextString();
                        try {
                            set = Integer.parseInt(stringValue) != 0;
                        } catch (NumberFormatException e) {
                            throw JsonSyntaxException("Error: Expecting: bitset number value (1, 0), Found: " + stringValue);
                        }
                        break;
                    default:
                        throw JsonSyntaxException("Invalid bitset value type: " + tokenType);
                }
                if (set) {
                    bitset.set(i);
                }
                ++i;
                tokenType = in.peek();
            }
            in.endArray();
            return bitset;
        }
    
        @Override
        public void write(JsonWriter out, BitSet src) throws IOException {
            if (src == null) {
                out.nullValue();
                return;
            }
            out.beginArray();
            for (int i = 0; i < src.length(); i++) {
                int value = (src.get(i)) ? 1 : 0;
                out.value(value);
            }
            out.endArray();
        }
    }
    BIT_SET_FACTORY = newFactory(BitSet.class, BIT_SET)
    BOOLEAN = TypeAdapter<Boolean>() {
    
        @Override
        public Boolean read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            } else if (in.peek() == JsonToken.STRING) {
                // support strings for compatibility with GSON 1.7
                return Boolean.parseBoolean(in.nextString());
            }
            return in.nextBoolean();
        }
    
        @Override
        public void write(JsonWriter out, Boolean value) throws IOException {
            out.value(value);
        }
    }
    BOOLEAN_AS_STRING = TypeAdapter<Boolean>() {
    
        @Override
        public Boolean read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            return Boolean.valueOf(in.nextString());
        }
    
        @Override
        public void write(JsonWriter out, Boolean value) throws IOException {
            out.value(value == null ? "null" : value.toString());
        }
    }
    """
    Writes a boolean as a string. Useful for map keys, where booleans aren't
    otherwise permitted.
    """
    BOOLEAN_FACTORY = newFactory(boolean.class, Boolean.class, BOOLEAN)
    BYTE = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                int intValue = in.nextInt();
                return (byte) intValue;
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    BYTE_FACTORY = newFactory(byte.class, Byte.class, BYTE)
    SHORT = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                return (short) in.nextInt();
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    SHORT_FACTORY = newFactory(short.class, Short.class, SHORT)
    INTEGER = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                return in.nextInt();
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    INTEGER_FACTORY = newFactory(int.class, Integer.class, INTEGER)
    ATOMIC_INTEGER = TypeAdapter<AtomicInteger>() {
    
        @Override
        public AtomicInteger read(JsonReader in) throws IOException {
            try {
                return AtomicInteger(in.nextInt());
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, AtomicInteger value) throws IOException {
            out.value(value.get());
        }
    }.nullSafe()
    ATOMIC_INTEGER_FACTORY = newFactory(AtomicInteger.class, TypeAdapters.ATOMIC_INTEGER)
    ATOMIC_BOOLEAN = TypeAdapter<AtomicBoolean>() {
    
        @Override
        public AtomicBoolean read(JsonReader in) throws IOException {
            return AtomicBoolean(in.nextBoolean());
        }
    
        @Override
        public void write(JsonWriter out, AtomicBoolean value) throws IOException {
            out.value(value.get());
        }
    }.nullSafe()
    ATOMIC_BOOLEAN_FACTORY = newFactory(AtomicBoolean.class, TypeAdapters.ATOMIC_BOOLEAN)
    ATOMIC_INTEGER_ARRAY = TypeAdapter<AtomicIntegerArray>() {
    
        @Override
        public AtomicIntegerArray read(JsonReader in) throws IOException {
            List<Integer> list = ArrayList<Integer>();
            in.beginArray();
            while (in.hasNext()) {
                try {
                    int integer = in.nextInt();
                    list.add(integer);
                } catch (NumberFormatException e) {
                    throw JsonSyntaxException(e);
                }
            }
            in.endArray();
            int length = list.size();
            AtomicIntegerArray array = AtomicIntegerArray(length);
            for (int i = 0; i < length; ++i) {
                array.set(i, list.get(i));
            }
            return array;
        }
    
        @Override
        public void write(JsonWriter out, AtomicIntegerArray value) throws IOException {
            out.beginArray();
            for (int i = 0, length = value.length(); i < length; i++) {
                out.value(value.get(i));
            }
            out.endArray();
        }
    }.nullSafe()
    ATOMIC_INTEGER_ARRAY_FACTORY = newFactory(AtomicIntegerArray.class, TypeAdapters.ATOMIC_INTEGER_ARRAY)
    LONG = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                return in.nextLong();
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    FLOAT = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            return (float) in.nextDouble();
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    DOUBLE = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            return in.nextDouble();
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    NUMBER = TypeAdapter<Number>() {
    
        @Override
        public Number read(JsonReader in) throws IOException {
            JsonToken jsonToken = in.peek();
            switch(jsonToken) {
                case NULL:
                    in.nextNull();
                    return null;
                case NUMBER:
                    return LazilyParsedNumber(in.nextString());
                default:
                    throw JsonSyntaxException("Expecting number, got: " + jsonToken);
            }
        }
    
        @Override
        public void write(JsonWriter out, Number value) throws IOException {
            out.value(value);
        }
    }
    NUMBER_FACTORY = newFactory(Number.class, NUMBER)
    CHARACTER = TypeAdapter<Character>() {
    
        @Override
        public Character read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            String str = in.nextString();
            if (str.length() != 1) {
                throw JsonSyntaxException("Expecting character, got: " + str);
            }
            return str.charAt(0);
        }
    
        @Override
        public void write(JsonWriter out, Character value) throws IOException {
            out.value(value == null ? null : String.valueOf(value));
        }
    }
    CHARACTER_FACTORY = newFactory(char.class, Character.class, CHARACTER)
    STRING = TypeAdapter<String>() {
    
        @Override
        public String read(JsonReader in) throws IOException {
            JsonToken peek = in.peek();
            if (peek == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            /* coerce booleans to strings for backwards compatibility */
            if (peek == JsonToken.BOOLEAN) {
                return Boolean.toString(in.nextBoolean());
            }
            return in.nextString();
        }
    
        @Override
        public void write(JsonWriter out, String value) throws IOException {
            out.value(value);
        }
    }
    BIG_DECIMAL = TypeAdapter<BigDecimal>() {
    
        @Override
        public BigDecimal read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                return BigDecimal(in.nextString());
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, BigDecimal value) throws IOException {
            out.value(value);
        }
    }
    BIG_INTEGER = TypeAdapter<BigInteger>() {
    
        @Override
        public BigInteger read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                return BigInteger(in.nextString());
            } catch (NumberFormatException e) {
                throw JsonSyntaxException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, BigInteger value) throws IOException {
            out.value(value);
        }
    }
    STRING_FACTORY = newFactory(String.class, STRING)
    STRING_BUILDER = TypeAdapter<StringBuilder>() {
    
        @Override
        public StringBuilder read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            return StringBuilder(in.nextString());
        }
    
        @Override
        public void write(JsonWriter out, StringBuilder value) throws IOException {
            out.value(value == null ? null : value.toString());
        }
    }
    STRING_BUILDER_FACTORY = newFactory(StringBuilder.class, STRING_BUILDER)
    STRING_BUFFER = TypeAdapter<StringBuffer>() {
    
        @Override
        public StringBuffer read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            return StringBuffer(in.nextString());
        }
    
        @Override
        public void write(JsonWriter out, StringBuffer value) throws IOException {
            out.value(value == null ? null : value.toString());
        }
    }
    STRING_BUFFER_FACTORY = newFactory(StringBuffer.class, STRING_BUFFER)
    URL = TypeAdapter<URL>() {
    
        @Override
        public URL read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            String nextString = in.nextString();
            return "null".equals(nextString) ? null : URL(nextString);
        }
    
        @Override
        public void write(JsonWriter out, URL value) throws IOException {
            out.value(value == null ? null : value.toExternalForm());
        }
    }
    URL_FACTORY = newFactory(URL.class, URL)
    URI = TypeAdapter<URI>() {
    
        @Override
        public URI read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            try {
                String nextString = in.nextString();
                return "null".equals(nextString) ? null : URI(nextString);
            } catch (URISyntaxException e) {
                throw JsonIOException(e);
            }
        }
    
        @Override
        public void write(JsonWriter out, URI value) throws IOException {
            out.value(value == null ? null : value.toASCIIString());
        }
    }
    URI_FACTORY = newFactory(URI.class, URI)
    INET_ADDRESS = TypeAdapter<InetAddress>() {
    
        @Override
        public InetAddress read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            // regrettably, this should have included both the host name and the host address
            return InetAddress.getByName(in.nextString());
        }
    
        @Override
        public void write(JsonWriter out, InetAddress value) throws IOException {
            out.value(value == null ? null : value.getHostAddress());
        }
    }
    INET_ADDRESS_FACTORY = newTypeHierarchyFactory(InetAddress.class, INET_ADDRESS)
    UUID = TypeAdapter<UUID>() {
    
        @Override
        public UUID read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            return java.util.UUID.fromString(in.nextString());
        }
    
        @Override
        public void write(JsonWriter out, UUID value) throws IOException {
            out.value(value == null ? null : value.toString());
        }
    }
    UUID_FACTORY = newFactory(UUID.class, UUID)
    CURRENCY = TypeAdapter<Currency>() {
    
        @Override
        public Currency read(JsonReader in) throws IOException {
            return Currency.getInstance(in.nextString());
        }
    
        @Override
        public void write(JsonWriter out, Currency value) throws IOException {
            out.value(value.getCurrencyCode());
        }
    }.nullSafe()
    CURRENCY_FACTORY = newFactory(Currency.class, CURRENCY)
    TIMESTAMP_FACTORY = TypeAdapterFactory() {
    
        // we use a runtime check to make sure the 'T's equal
        @SuppressWarnings("unchecked")
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> typeToken) {
            if (typeToken.getRawType() != Timestamp.class) {
                return null;
            }
            final TypeAdapter<Date> dateTypeAdapter = gson.getAdapter(Date.class);
            return (TypeAdapter<T>) TypeAdapter<Timestamp>() {
    
                @Override
                public Timestamp read(JsonReader in) throws IOException {
                    Date date = dateTypeAdapter.read(in);
                    return date != null ? Timestamp(date.getTime()) : null;
                }
    
                @Override
                public void write(JsonWriter out, Timestamp value) throws IOException {
                    dateTypeAdapter.write(out, value);
                }
            };
        }
    }
    CALENDAR = TypeAdapter<Calendar>() {
    
        private static final String YEAR = "year";
    
        private static final String MONTH = "month";
    
        private static final String DAY_OF_MONTH = "dayOfMonth";
    
        private static final String HOUR_OF_DAY = "hourOfDay";
    
        private static final String MINUTE = "minute";
    
        private static final String SECOND = "second";
    
        @Override
        public Calendar read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            in.beginObject();
            int year = 0;
            int month = 0;
            int dayOfMonth = 0;
            int hourOfDay = 0;
            int minute = 0;
            int second = 0;
            while (in.peek() != JsonToken.END_OBJECT) {
                String name = in.nextName();
                int value = in.nextInt();
                if (YEAR.equals(name)) {
                    year = value;
                } else if (MONTH.equals(name)) {
                    month = value;
                } else if (DAY_OF_MONTH.equals(name)) {
                    dayOfMonth = value;
                } else if (HOUR_OF_DAY.equals(name)) {
                    hourOfDay = value;
                } else if (MINUTE.equals(name)) {
                    minute = value;
                } else if (SECOND.equals(name)) {
                    second = value;
                }
            }
            in.endObject();
            return GregorianCalendar(year, month, dayOfMonth, hourOfDay, minute, second);
        }
    
        @Override
        public void write(JsonWriter out, Calendar value) throws IOException {
            if (value == null) {
                out.nullValue();
                return;
            }
            out.beginObject();
            out.name(YEAR);
            out.value(value.get(Calendar.YEAR));
            out.name(MONTH);
            out.value(value.get(Calendar.MONTH));
            out.name(DAY_OF_MONTH);
            out.value(value.get(Calendar.DAY_OF_MONTH));
            out.name(HOUR_OF_DAY);
            out.value(value.get(Calendar.HOUR_OF_DAY));
            out.name(MINUTE);
            out.value(value.get(Calendar.MINUTE));
            out.name(SECOND);
            out.value(value.get(Calendar.SECOND));
            out.endObject();
        }
    }
    CALENDAR_FACTORY = newFactoryForMultipleTypes(Calendar.class, GregorianCalendar.class, CALENDAR)
    LOCALE = TypeAdapter<Locale>() {
    
        @Override
        public Locale read(JsonReader in) throws IOException {
            if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;
            }
            String locale = in.nextString();
            StringTokenizer tokenizer = StringTokenizer(locale, "_");
            String language = null;
            String country = null;
            String variant = null;
            if (tokenizer.hasMoreElements()) {
                language = tokenizer.nextToken();
            }
            if (tokenizer.hasMoreElements()) {
                country = tokenizer.nextToken();
            }
            if (tokenizer.hasMoreElements()) {
                variant = tokenizer.nextToken();
            }
            if (country == null && variant == null) {
                return Locale(language);
            } else if (variant == null) {
                return Locale(language, country);
            } else {
                return Locale(language, country, variant);
            }
        }
    
        @Override
        public void write(JsonWriter out, Locale value) throws IOException {
            out.value(value == null ? null : value.toString());
        }
    }
    LOCALE_FACTORY = newFactory(Locale.class, LOCALE)
    JSON_ELEMENT = TypeAdapter<JsonElement>() {
    
        @Override
        public JsonElement read(JsonReader in) throws IOException {
            switch(in.peek()) {
                case STRING:
                    return JsonPrimitive(in.nextString());
                case NUMBER:
                    String number = in.nextString();
                    return JsonPrimitive(LazilyParsedNumber(number));
                case BOOLEAN:
                    return JsonPrimitive(in.nextBoolean());
                case NULL:
                    in.nextNull();
                    return JsonNull.INSTANCE;
                case BEGIN_ARRAY:
                    JsonArray array = JsonArray();
                    in.beginArray();
                    while (in.hasNext()) {
                        array.add(read(in));
                    }
                    in.endArray();
                    return array;
                case BEGIN_OBJECT:
                    JsonObject object = JsonObject();
                    in.beginObject();
                    while (in.hasNext()) {
                        object.add(in.nextName(), read(in));
                    }
                    in.endObject();
                    return object;
                case END_DOCUMENT:
                case NAME:
                case END_OBJECT:
                case END_ARRAY:
                default:
                    throw IllegalArgumentException();
            }
        }
    
        @Override
        public void write(JsonWriter out, JsonElement value) throws IOException {
            if (value == null || value.isJsonNull()) {
                out.nullValue();
            } else if (value.isJsonPrimitive()) {
                JsonPrimitive primitive = value.getAsJsonPrimitive();
                if (primitive.isNumber()) {
                    out.value(primitive.getAsNumber());
                } else if (primitive.isBoolean()) {
                    out.value(primitive.getAsBoolean());
                } else {
                    out.value(primitive.getAsString());
                }
            } else if (value.isJsonArray()) {
                out.beginArray();
                for (JsonElement e : value.getAsJsonArray()) {
                    write(out, e);
                }
                out.endArray();
            } else if (value.isJsonObject()) {
                out.beginObject();
                for (Map.Entry<String, JsonElement> e : value.getAsJsonObject().entrySet()) {
                    out.name(e.getKey());
                    write(out, e.getValue());
                }
                out.endObject();
            } else {
                throw IllegalArgumentException("Couldn't write " + value.getClass());
            }
        }
    }
    JSON_ELEMENT_FACTORY = newTypeHierarchyFactory(JsonElement.class, JSON_ELEMENT)
    ENUM_FACTORY = TypeAdapterFactory() {
    
        @SuppressWarnings({ "rawtypes", "unchecked" })
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> typeToken) {
            Class<? super T> rawType = typeToken.getRawType();
            if (!Enum.class.isAssignableFrom(rawType) || rawType == Enum.class) {
                return null;
            }
            if (!rawType.isEnum()) {
                // handle anonymous subclasses
                rawType = rawType.getSuperclass();
            }
            return (TypeAdapter<T>) EnumTypeAdapter(rawType);
        }
    }


    @staticmethod
    def newFactory(type: "TypeToken"["TT"], typeAdapter: "TypeAdapter"["TT"]) -> "TypeAdapterFactory":
        ...


    @staticmethod
    def newFactory(type: type["TT"], typeAdapter: "TypeAdapter"["TT"]) -> "TypeAdapterFactory":
        ...


    @staticmethod
    def newFactory(unboxed: type["TT"], boxed: type["TT"], typeAdapter: "TypeAdapter"["TT"]) -> "TypeAdapterFactory":
        ...


    @staticmethod
    def newFactoryForMultipleTypes(base: type["TT"], sub: type["TT"], typeAdapter: "TypeAdapter"["TT"]) -> "TypeAdapterFactory":
        ...


    @staticmethod
    def newTypeHierarchyFactory(clazz: type["T1"], typeAdapter: "TypeAdapter"["T1"]) -> "TypeAdapterFactory":
        """
        Returns a factory for all subtypes of `typeAdapter`. We do a runtime check to confirm
        that the deserialized type matches the type requested.
        """
        ...
